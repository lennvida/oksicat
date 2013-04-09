# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Upload'
        db.create_table('core_upload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('file', self.gf('triadatv.core.utils.upload.UploadField')(max_length=100)),
            ('is_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Upload'])

        # Adding model 'Promo'
        db.create_table('core_promo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=550, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=550, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Promo'])


    def backwards(self, orm):
        # Deleting model 'Upload'
        db.delete_table('core_upload')

        # Deleting model 'Promo'
        db.delete_table('core_promo')


    models = {
        'core.promo': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Promo'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '550', 'blank': 'True'}),
            'type': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '550', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'core.upload': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Upload'},
            'file': ('triadatv.core.utils.upload.UploadField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['core']