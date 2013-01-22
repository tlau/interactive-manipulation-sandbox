from django.shortcuts import render_to_response

from rest_framework import status
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from world.models import BIFAction, BIFProgram
from serializers import ProgramSerializer

import logging
from world.robot import get_robot_proxy
from world.models import API_call_choices

API_names = [c[0] for c in API_call_choices]
logger = logging.getLogger('dev')


def index(request):
    return render_to_response('index.html', {'user': request.user})


# "programs" endpoint.

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def single_program(request, pk, format=None):
    """Operate on a single program.

    TODO: implement as a class based view; the REST framework can reduce this
    code to three small methods.
    """

    program = BIFProgram.objects.get(pk=pk)
    if request.method == 'GET':
        # Get the program from the system.
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Replace the program with the edited version (JSON encoded).
        try:
            program_data = request.DATA
            # new_program_data = json.loads(data)
            new_name = program_data['name']
            steps_data = program_data['steps']
            new_steps = []
            for action_dict in steps_data:
                new_steps.append(BIFAction.from_dict(action_dict))

        except (ValueError, KeyError, TypeError) as e:
            # KeyError: POSTed data does not have a "program" data.
            # ValueError: POSTed program had invalid JSON format.
            # ValueError: interpreted program is not a BIF program.
            logger.debug('Exception reading a program: %s' % e)
            reason = {
                'details': "Bad program format: %s" % e
                }
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)
        program.name = new_name
        program.replace_step_sequence(new_steps)
        program.save()
        serializer = ProgramSerializer(program)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # Deleting a program deletes all of its steps.
        program.delete()
        return Response(status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def programs(request, format=None):
    """Operate on the collection of programs.

    TODO: implement as a class based view; the REST framework can reduce this
    code to three small methods.
    """
    if request.method == 'GET':
        # Get all the programs from the system.
        programs = BIFProgram.objects.all()
        serializer = ProgramSerializer(programs)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Add a new program to the system.
        try:
            program_data = request.DATA
            new_name = program_data['name']

            instructions_data = program_data['instructions']
            new_instructions = []
            instruction_index = 0
            for action_dict in instructions_data:
                instruction_index += 1
                # Don't save the new BIF Actions until they pass parsing.
                action = BIFAction.from_dict(action_dict)
                action.instruction_number = instruction_index
                new_instructions.append(action)
        except (ValueError, TypeError, KeyError) as e:
            # KeyError, TypeError: POSTed data has bad shape.
            # ValueError: interpreted program is not a BIF program.
            logger.debug('Exception creating new program: %s' % e)
            reason = {
                'detail': "Bad program format: %s" % e,
                }
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        program = BIFProgram(name=new_name)
        program.save()
        # Assign and save the instructions.
        program.replace_instruction_sequence(new_instructions)
        serializer = ProgramSerializer(program)
        return Response(serializer.data, status.HTTP_200_OK)


# interpreter endpoint.

# The strategy to run client sent code on the robot is the following:
# 1. turn the client code into a python data type.
# 2. apply appropriate data transforms to the results to get a "data program".
# 3. verify it is a valid data program:
#   * program has steps,
#   * for each step
#     * action name is a correct API call.
#     * params are correct for for that action.
# 4. Verify the robot is available to execute program.
# 5. Make the action function call.
#   * expect exceptions.
#   * recover robot from inconsistent state.
#   * return error data to the user.
# 6. Bring the robot to a state capable of receiving the next program.
# 7. Release any resources used.
# 8. Pop the champagne.

@api_view(['POST'])
@parser_classes([JSONParser])
def run_program(request):
    """Run the program POSTed, without saving it."""

    # NOTE 1:
    # Trust that the POSTed program is valid.

    program = request.DATA
    logger.info('Excuting program "%s".' % program['name'])

    # NOTE 2:
    # In order to test the model-related code, the program POSTed is persisted
    # (along with all its steps) before being run, and immediatly after the
    # execution finished (whether successful or not), the program (and its
    # steps) is deleted.
    #
    # To acomplish this, the POSTed data is first passed to the models
    # (converting from its 'dict' representation), then from the models to the
    # robot_api_call() (converting to its 'dict' representation). Silly thing.

    # Convert dict repr's into BIFAction instances.
    try:
        # Create objects without save()'ing the to the database yet.
        bif_actions = [BIFAction.from_dict(step) for step in program['steps']]
    except (TypeError, ValueError) as e:
        msg = ('Failed to create a BIFAction from dict representation: %s' % e)
        logger.debug(msg)
        return Response({'detail': msg},
                        status=status.HTTP_400_BAD_REQUEST)
    # The following code creates the (temporary) database entities.
    bif_program = BIFProgram(name=program['name'])
    bif_program.save()
    bif_program.replace_step_sequence(bif_actions)

    # Convert BIFAction instances into dict repr's.
    steps = [action.to_dict() for action in bif_actions]

    try:

        for step in steps:
            # Pick on the dict repr of the step, to produce the API call.

            fn_name = step['action']
            if fn_name not in API_names:
                msg = ('Bad API call (%s) from program "%s".'
                       % (fn_name, program['name']))
                logger.debug(msg)
                return Response({'detail': msg},
                                status=status.HTTP_400_BAD_REQUEST)

            robot = get_robot_proxy()
            robot_api_call = getattr(robot, fn_name)
            params = step['params']

            try:

                # ...Blocking call...
                robot_api_call(**params)

            except (TypeError, ValueError) as e:
                msg = ('API call "%s", bad parameters: %s'
                       % (fn_name, params))
                logger.debug(msg)
                return Response({'detail': msg, 'exception': '%s' % e},
                                status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                msg = ('API call "%s", exception: %s'
                       % (fn_name, e))
                logger.debug(msg)
                return Response({'detail': msg},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            finally:
                # Run clean up on the robot.
                pass
    finally:
        # Clean up the temporary database entities.
        bif_program.delete()  # mean cascade kills all actions.

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([JSONParser])
def run_step(request):
    """Run the step POSTed alone, without saving it."""

    # Trust that the POSTed step is valid.
    step = request.DATA

    fn_name = step['action']
    if fn_name not in API_names:
        msg = ('Bad API call (%s).' % fn_name)
        logger.debug(msg)
        return Response({'detail': msg},
                        status=status.HTTP_400_BAD_REQUEST)

    robot_api_call = getattr(robot, fn_name)
    params = step['params']
    try:

        # ... Blocking call...
        robot_api_call(params)

    except (TypeError, ValueError):
        msg = ('API call %s, bad parameters: %s'
               % (fn_name, params))
        logger.debug(msg)
        return Response({'detail': msg},
                        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        msg = ('API call %s, exception: %s'
               % (fn_name, e))
        logger.debug(msg)
        return Response({'detail': msg},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        # Run clean up on the robot.
        pass
    return Response(status=status.HTTP_200_OK)
