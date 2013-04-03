# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StructureNode'
        db.create_table('structure_structurenode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('menu_type', self.gf('django.db.models.fields.CharField')(default='main', max_length=100)),
            ('menu', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('menu_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('teaser', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('header_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('index_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['structure.StructureNode'])),
            ('template', self.gf('django.db.models.fields.CharField')(default='default.html', max_length=100)),
            ('redirect_url', self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1000)),
            ('left', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('right', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('structure', ['StructureNode'])

        # Adding model 'StructureNodeExtendField'
        db.create_table('structure_structurenodeextendfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='extend_fields', to=orm['structure.StructureNode'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('structure', ['StructureNodeExtendField'])

        # Adding unique constraint on 'StructureNodeExtendField', fields ['structure_node', 'name']
        db.create_unique('structure_structurenodeextendfield', ['structure_node_id', 'name'])

        # Adding model 'RightBlock'
        db.create_table('structure_rightblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure_node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='right_blocks', to=orm['structure.StructureNode'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('structure', ['RightBlock'])

        # Adding model 'Upload'
        db.create_table('structure_upload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('file', self.gf('triadatv.core.utils.upload.UploadField')(max_length=100)),
            ('is_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('structure', ['Upload'])

        # Adding model 'Promo'
        db.create_table('structure_promo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=550, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('structure', ['Promo'])


    def backwards(self, orm):
        # Removing unique constraint on 'StructureNodeExtendField', fields ['structure_node', 'name']
        db.delete_unique('structure_structurenodeextendfield', ['structure_node_id', 'name'])

        # Deleting model 'StructureNode'
        db.delete_table('structure_structurenode')

        # Deleting model 'StructureNodeExtendField'
        db.delete_table('structure_structurenodeextendfield')

        # Deleting model 'RightBlock'
        db.delete_table('structure_rightblock')

        # Deleting model 'Upload'
        db.delete_table('structure_upload')

        # Deleting model 'Promo'
        db.delete_table('structure_promo')


    models = {
        'structure.promo': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Promo'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '550', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
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
            'index_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'menu_type': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '100'}),
            'menu_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['structure.StructureNode']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1000'}),
            'redirect_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'right': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'teaser': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
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
        },
        'structure.upload': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Upload'},
            'file': ('triadatv.core.utils.upload.UploadField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['structure']