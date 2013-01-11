# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('world_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pose_x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pose_y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pose_angle', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('map_x', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_y', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('world', ['Place'])

        # Adding model 'Camera'
        db.create_table('world_camera', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('features', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('world', ['Camera'])

        # Adding model 'Robot'
        db.create_table('world_robot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')()),
            ('service_url', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('camera_base_url', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('world', ['Robot'])

        # Adding M2M table for field cameras on 'Robot'
        db.create_table('world_robot_cameras', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('robot', models.ForeignKey(orm['world.robot'], null=False)),
            ('camera', models.ForeignKey(orm['world.camera'], null=False))
        ))
        db.create_unique('world_robot_cameras', ['robot_id', 'camera_id'])

        # Adding model 'Client'
        db.create_table('world_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('context', self.gf('django.db.models.fields.TextField')()),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('world', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('world_place')

        # Deleting model 'Camera'
        db.delete_table('world_camera')

        # Deleting model 'Robot'
        db.delete_table('world_robot')

        # Removing M2M table for field cameras on 'Robot'
        db.delete_table('world_robot_cameras')

        # Deleting model 'Client'
        db.delete_table('world_client')


    models = {
        'world.camera': {
            'Meta': {'object_name': 'Camera'},
            'features': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'world.client': {
            'Meta': {'object_name': 'Client'},
            'context': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'world.place': {
            'Meta': {'object_name': 'Place'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'map_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_x': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'map_y': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'pose_angle': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pose_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pose_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'world.robot': {
            'Meta': {'object_name': 'Robot'},
            'camera_base_url': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cameras': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['world.Camera']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'public': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'service_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'state': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['world']