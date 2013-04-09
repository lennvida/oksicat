# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Upload'
        db.delete_table('structure_upload')

        # Deleting model 'Promo'
        db.delete_table('structure_promo')

        # Deleting field 'StructureNode.index_image'
        db.delete_column('structure_structurenode', 'index_image')

        # Deleting field 'StructureNode.teaser'
        db.delete_column('structure_structurenode', 'teaser')

        # Deleting field 'StructureNode.menu_type'
        db.delete_column('structure_structurenode', 'menu_type')


    def backwards(self, orm):
        # Adding model 'Upload'
        db.create_table('structure_upload', (
            ('is_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('file', self.gf('triadatv.core.utils.upload.UploadField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('structure', ['Upload'])

        # Adding model 'Promo'
        db.create_table('structure_promo', (
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=550, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=550, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('structure', ['Promo'])

        # Adding field 'StructureNode.index_image'
        db.add_column('structure_structurenode', 'index_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StructureNode.teaser'
        db.add_column('structure_structurenode', 'teaser',
                      self.gf('tinymce.models.HTMLField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'StructureNode.menu_type'
        db.add_column('structure_structurenode', 'menu_type',
                      self.gf('django.db.models.fields.CharField')(default='main', max_length=100),
                      keep_default=False)


    models = {
        'structure.rightblock': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'RightBlock'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'structure_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'right_blocks'", 'to': "orm['structure.StructureNode']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'structure.structurenode': {
            'Meta': {'ordering': "('tree_id', 'left')", 'object_name': 'StructureNode'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'menu_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['structure.StructureNode']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'redirect_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'right': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'default.html'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'structure.structurenodeextendfield': {
            'Meta': {'unique_together': "(('structure_node', 'name'),)", 'object_name': 'StructureNodeExtendField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'structure_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'extend_fields'", 'to': "orm['structure.StructureNode']"}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['structure']