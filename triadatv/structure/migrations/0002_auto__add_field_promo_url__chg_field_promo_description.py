# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Promo.url'
        db.add_column('structure_promo', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=550, blank=True),
                      keep_default=False)


        # Changing field 'Promo.description'
        db.alter_column('structure_promo', 'description', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):
        # Deleting field 'Promo.url'
        db.delete_column('structure_promo', 'url')


        # Changing field 'Promo.description'
        db.alter_column('structure_promo', 'description', self.gf('django.db.models.fields.TextField')())

    models = {
        'structure.promo': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Promo'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '550', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '550', 'blank': 'True'}),
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