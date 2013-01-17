from rest_framework import serializers, generics
from django.conf.urls.defaults import patterns, url

from world.models import Pose, BinLocation, BIFProgram, BIFAction
import world.views


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


urlpatterns = patterns('',
    url(r'^binlocations$', generics.ListAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),
    url(r'^binlocations/(?P<pk>[^/]+)$', generics.RetrieveAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),

    url(r'^programs$', world.views.programs),
    url(r'^programs/(?P<pk>[^/]+)$', world.views.single_program),
)
