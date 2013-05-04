# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Marker.default'
        db.add_column('map_marker', 'default',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Marker.default'
        db.delete_column('map_marker', 'default')


    models = {
        'map.marker': {
            'Meta': {'object_name': 'Marker'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['map']