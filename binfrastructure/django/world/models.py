from django.db import models
from django.conf import settings

class Place(models.Model):
    name = models.TextField()
    tags = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="images",blank=True,null=True)

    pose_x = models.FloatField(blank=True,null=True)
    pose_y = models.FloatField(blank=True,null=True)
    pose_angle = models.FloatField(blank=True,null=True)

    map_x = models.IntegerField(blank=True,null=True)
    map_y = models.IntegerField(blank=True,null=True)
    map_width = models.IntegerField(blank=True,null=True)
    map_height = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class Camera(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=512)

    # Features this camera is available for. It consists of a string of single
    # space separated words, each a feature identifier (e.g. "look pick-up").
    features = models.CharField(max_length=512, blank=True, null=False)

    def __unicode__(self):
        return self.url

class Robot(models.Model):
    name = models.TextField()
    tags = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="images",blank=True,null=True)

    public = models.NullBooleanField(blank=True,null=True)

    state = models.IntegerField(choices=(
        (0,'Idle'), (1,'Busy'),
    ))

    # Disabled using URLFields since for the time being they do not support
    # Web Socket addresses
    #service_url = models.URLField(verify_exists=False)     # URL to robot's rosbridge instance
    #camera_url = models.URLField(verify_exists=False)      # URL to mjpeg output for Robot's camera
    service_url = models.CharField(max_length=512)     # URL to robot's rosbridge instance
#    camera_url = models.CharField(max_length=512)      # URL to mjpeg output for Robot's camera
#    forearm_camera_url = models.CharField(max_length=512)      # URL to mjpeg output for Robot's forearm camera
    camera_base_url = models.CharField(max_length=128)
    cameras = models.ManyToManyField(Camera)
