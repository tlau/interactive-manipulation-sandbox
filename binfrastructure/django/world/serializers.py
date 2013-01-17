from rest_framework import serializers
from world.models import Pose, BinLocation, BIFProgram, BIFAction


class ExplicitPoseSerializer(serializers.ModelSerializer):
    """Serialize the pose data, and only that."""
    class Meta:
        model = Pose
        exclude = ('id',)


class BinLocationSerializer(serializers.ModelSerializer):
    pose = ExplicitPoseSerializer(source='pose')

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
