# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedbackManager'
        db.create_table('feedback_feedbackmanager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('feedback', ['FeedbackManager'])

        # Adding model 'FeedbackFormManager'
        db.create_table('feedback_feedbackformmanager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('feedback', ['FeedbackFormManager'])

        # Adding M2M table for field email on 'FeedbackFormManager'
        db.create_table('feedback_feedbackformmanager_email', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feedbackformmanager', models.ForeignKey(orm['feedback.feedbackformmanager'], null=False)),
            ('feedbackmanager', models.ForeignKey(orm['feedback.feedbackmanager'], null=False))
        ))
        db.create_unique('feedback_feedbackformmanager_email', ['feedbackformmanager_id', 'feedbackmanager_id'])


    def backwards(self, orm):
        # Deleting model 'FeedbackManager'
        db.delete_table('feedback_feedbackmanager')

        # Deleting model 'FeedbackFormManager'
        db.delete_table('feedback_feedbackformmanager')

        # Removing M2M table for field email on 'FeedbackFormManager'
        db.delete_table('feedback_feedbackformmanager_email')


    models = {
        'feedback.feedbackformmanager': {
            'Meta': {'ordering': "['caption']", 'object_name': 'FeedbackFormManager'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['feedback.FeedbackManager']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'feedback.feedbackmanager': {
            'Meta': {'ordering': "['email']", 'object_name': 'FeedbackManager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']