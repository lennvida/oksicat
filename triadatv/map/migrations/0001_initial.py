# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Marker'
        db.create_table('map_marker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')()),
            ('y', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('map', ['Marker'])


    def backwards(self, orm):
        # Deleting model 'Marker'
        db.delete_table('map_marker')


    models = {
        'map.marker': {
            'Meta': {'object_name': 'Marker'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['map']