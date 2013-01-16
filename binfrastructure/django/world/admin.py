from django.contrib import admin
import world.models


class BinAdmin(admin.ModelAdmin):
    exclude = ['pose_last_seen', 'time_last_seen']

admin.site.register(world.models.Pose)
admin.site.register(world.models.BinLocation)
admin.site.register(world.models.Bin, BinAdmin)
