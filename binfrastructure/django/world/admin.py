from django.contrib import admin
from world.models import Place, Robot, Camera

class RobotAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'pose_x', 'pose_y', 'map_x', 'map_y')

class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(Camera, CameraAdmin)
