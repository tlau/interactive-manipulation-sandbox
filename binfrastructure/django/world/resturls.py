import logging
from rest_framework import status, generics, serializers
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.conf.urls.defaults import patterns, url
from world.models import Pose, BinLocation, BIFProgram, BIFAction

logger = logging.getLogger('dev')


class ExplicitPoseSerializer(serializers.ModelSerializer):
    """Serialize the pose data, and only that."""
    class Meta:
        model = Pose
        exclude = ('id',)


class BinLocationSerializer(serializers.ModelSerializer):
    pickup_dropoff_pose = ExplicitPoseSerializer(source='pickup_dropoff_pose')

    class Meta:
        model = BinLocation


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = BIFAction
        exclude = ['id', 'program', 'step_number']


class ProgramSerializer(serializers.ModelSerializer):

    steps = StepSerializer(source='step_sequence')

    class Meta:
        model = BIFProgram
        # Serialize BIFActions composing this program.
        depth = 1


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

        except (ValueError, KeyError) as e:
            # KeyError: POSTed data does not have a "program" data.
            # ValueError: POSTed program had invalid JSON format.
            # ValueError: interpreted program is not a BIF program.
            logger.debug('Exception serializing a program: %s' % e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
        except (ValueError, TypeError) as e:
            # TypeError: POSTed data does not have "name"/""instructions" data.
            # ValueError: interpreted program is not a BIF program.
            logger.debug('Exception creating new program: %s' % e)
            reason = {
                'detail': "Bad program format."
                }
            return Response(reason, status=status.HTTP_400_BAD_REQUEST)

        program = BIFProgram(name=new_name)
        program.save()
        # Assign and save the instructions.
        program.replace_instruction_sequence(new_instructions)
        serializer = ProgramSerializer(program)
        return Response(serializer.data, status.HTTP_200_OK)


urlpatterns = patterns('',
    url(r'^binlocations$', generics.ListAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),
    url(r'^binlocations/(?P<pk>[^/]+)$', generics.RetrieveAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),

    url(r'^programs$', programs),
    url(r'^programs/(?P<pk>[^/]+)$', single_program),
)
