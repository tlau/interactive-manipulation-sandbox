# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models



class Migration(DataMigration):

    # This is the data intruduced/removed by this migration.
    new_data = [
        {'name': 'kitchen',
         'pose': {'x': 1.0, 'y': 1.0, 'angle': 0.5}},
        {'name': 'garage',
         'pose': {'x': 3.0, 'y': 2.0, 'angle': 3.8}},
        {'name': 'cathedral',
         'pose': {'x': 3.1, 'y': 3.3, 'angle': 7}},
    ]

    def forwards(self, orm):
        for location in self.new_data:
            # create the pose
            pose_data = location['pose']
            pose = orm['world.Pose'](**pose_data)
            pose.save()
            # create the location at that pose.
            orm['world.BinLocation'](name=location['name'],
                                     pickup_dropoff_pose=pose).save()

    def backwards(self, orm):
        for location in self.new_data:
            binlocation = orm['world.BinLocation'].objects.get(name=location['name'])
            # the CASCADE database strategy will delete the pose too.
            binlocation.delete()

    models = {
        'world.bifaction': {
            'Meta': {'object_name': 'BIFAction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'world.bin': {
            'Meta': {'object_name': 'Bin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_empty': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bins'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['world.BinLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pose_last_seen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Pose']", 'null': 'True'}),
            'time_last_seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'world.binlocation': {
            'Meta': {'object_name': 'BinLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pickup_dropoff_pose': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['world.Pose']", 'unique': 'True'})
        },
        'world.pose': {
            'Meta': {'object_name': 'Pose'},
            'angle': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'y': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['world']
    symmetrical = True
