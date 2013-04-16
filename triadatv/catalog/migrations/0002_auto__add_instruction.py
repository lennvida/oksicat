# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instruction'
        db.create_table('catalog_instruction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Item'])),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('catalog', ['Instruction'])


    def backwards(self, orm):
        # Deleting model 'Instruction'
        db.delete_table('catalog_instruction')


    models = {
        'catalog.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Item']"}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        'catalog.item': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Item'},
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['catalog']