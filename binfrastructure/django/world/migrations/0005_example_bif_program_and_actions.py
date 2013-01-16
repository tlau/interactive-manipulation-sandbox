# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    PROGRAM_NAME = 'example program'
    ACTIONS = [
        {
            'name': 'speak',
            'params_string': "hi there :)",
        },
        {
            'name': 'wait',
            'params_string': "3.0",
        },
        {
            'name': 'speak',
            'params_string': "ok, bye!",
        },
    ]

    def forwards(self, orm):
        # Create an example program.
        program = orm['world.BIFProgram'](name=self.PROGRAM_NAME)
        program.save()
        # Add actions to the example program.
        instruction_pointer = 0
        for action_data in self.ACTIONS:
            instruction_pointer += 1
            action = orm['world.BIFAction'](
                name=action_data['name'],
                params=action_data['params_string']
            )
            action.program = program
            action.instruction_number = instruction_pointer
            action.save()

    def backwards(self, orm):
        # Relying on CASCADE strategy is dangerous here...
        # Delete each instruction in the program separately.
        program = orm['world.BIFProgram'].objects.get(name=self.PROGRAM_NAME)
        for action in program.instructions.all():
            action.delete()
        program.delete()

    models = {
        'world.bifaction': {
            'Meta': {'object_name': 'BIFAction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'params': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'instructions'", 'null': 'True', 'to': "orm['world.BIFProgram']"})
        },
        'world.bifprogram': {
            'Meta': {'object_name': 'BIFProgram'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
