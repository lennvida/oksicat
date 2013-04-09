# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table('forum_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=42)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('tinymce.models.HTMLField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forum.Message'], null=True, blank=True)),
        ))
        db.send_create_signal('forum', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('forum_message')


    models = {
        'forum.message': {
            'Meta': {'ordering': "('-datetime',)", 'object_name': 'Message'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forum.Message']", 'null': 'True', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['forum']