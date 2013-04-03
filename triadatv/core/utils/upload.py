# -*- coding: utf-8 -*-

import mimetypes
from south.modelsinspector import add_introspection_rules

from django import forms
from django.core.files.images import ImageFile, get_image_dimensions
from django.db.models.fields.files import FieldFile, ImageField

add_introspection_rules([], ["^triadatv\.core\.utils\.upload\.UploadField"])

class UploadFieldFile(ImageFile, FieldFile):

    def save(self, name, content, save=True):

        if self.is_image():
            self._dimensions_cache = get_image_dimensions(content)

            if self.field.width_field:
                setattr(self.instance, self.field.width_field, self.width)
            if self.field.height_field:
                setattr(self.instance, self.field.height_field, self.height)

        super(UploadFieldFile, self).save(name, content, save)

    def delete(self, save=True):
        # Clear the image dimensions cache
        if hasattr(self, '_dimensions_cache'):
            del self._dimensions_cache
        super(UploadFieldFile, self).delete(save)

    def is_image(self):
        try:
            p1, p2 = mimetypes.guess_type(self.name)[0].split('/')
            if p1 == 'image' and p2 in ('jpeg', 'png', 'gif', 'tiff'):
                return True 
        except AttributeError:
            pass
        return False

    def is_swf(self):
        try:
            return mimetypes.guess_type(self.name)[0] == 'application/x-shockwave-flash'
        except AttributeError:
            return False

class UploadField(ImageField):

    attr_class = UploadFieldFile

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.FileField}
        defaults.update(kwargs)
        return super(ImageField, self).formfield(**defaults)