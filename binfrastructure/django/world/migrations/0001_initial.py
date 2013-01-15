# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pose'
        db.create_table('world_pose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('y', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('angle', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('world', ['Pose'])

        # Adding model 'BinLocation'
        db.create_table('world_binlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pickup_dropoff_pose', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['world.Pose'], unique=True)),
        ))
        db.send_create_signal('world', ['BinLocation'])

        # Adding model 'Bin'
        db.create_table('world_bin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('is_empty', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bins', null=True, on_delete=models.SET_NULL, to=orm['world.BinLocation'])),
            ('pose_last_seen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Pose'], null=True)),
            ('time_last_seen', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('world', ['Bin'])


    def backwards(self, orm):
        # Deleting model 'Pose'
        db.delete_table('world_pose')

        # Deleting model 'BinLocation'
        db.delete_table('world_binlocation')

        # Deleting model 'Bin'
        db.delete_table('world_bin')


    models = {
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