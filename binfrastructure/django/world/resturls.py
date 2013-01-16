from rest_framework import generics, serializers
from django.conf.urls.defaults import patterns, url
from models import Pose, BinLocation


class ExplicitPoseSerializer(serializers.ModelSerializer):
    """Serialize the pose data, and only that."""
    class Meta:
        model = Pose
        exclude = ('id',)


class BinLocationSerializer(serializers.ModelSerializer):
    pickup_dropoff_pose = ExplicitPoseSerializer(source='pickup_dropoff_pose')

    class Meta:
        model = BinLocation


urlpatterns = patterns('',
    url(r'^binlocations$', generics.ListAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),
    url(r'^binlocations/(?P<pk>[^/]+)$', generics.RetrieveAPIView.as_view(
        model=BinLocation,
        serializer_class=BinLocationSerializer)),
)
