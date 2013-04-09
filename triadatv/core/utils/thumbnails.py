# -*- coding: utf-8 -*-

from PIL import Image
import math
import os.path

from django.conf import settings

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

METHOD_LIST = [
    'crop',
]

class Thumbnail(object):

    crop = False
    quality = [98]

    store_dir = settings.THUMBNAIL_DIR
    store_url = settings.THUMBNAIL_URL

    def __init__(self, filename, **kwargs):
        options = dict(getattr(settings, 'THUMBNAIL_DEFAULTS', {}))
        options.update(kwargs)
        for k,v in options.items():
            setattr(self, k, v)
        if os.path.isabs(filename):
            self.filename = filename
        else:
            self.filename = os.path.join(settings.MEDIA_ROOT, filename)
        if not os.path.isfile(os.path.realpath(self.filename)):
            raise Exception("File '%s' does not exist." % filename)
        if not self.is_valid_thumbnail():
            self.make_thumbnail()

    def is_valid_thumbnail(self):
        if not os.path.isfile(self.thumbnail_filename):
            return False
        if os.path.getmtime(self.filename) > os.path.getmtime(self.thumbnail_filename):
            return False
        return True

    def get_thumbnail_filename(self):
        if getattr(self, '_thumbnail_filename', None) is None:
            filename = '%s.png' % (self.get_hash(), )
            if not os.path.exists(self.store_dir):
                os.mkdir(self.store_dir)
            self._thumbnail_filename = os.path.join(self.store_dir, filename)
        return self._thumbnail_filename
    thumbnail_filename = property(get_thumbnail_filename)

    def get_hash(self):
        hash = []
        for attr in ['filename', 'out_size', 'quality', ] + METHOD_LIST:
            hash.append(getattr(self, attr, False))
        return md5(unicode(hash)).hexdigest()

    def make_thumbnail(self):
        try:
            image = Image.open(self.filename)
            image = image.convert("RGBA")
        except IOError, detail:
            raise Exception(detail)

        w, h = [float(i) for i in image.size]
        out_w = float(self.out_size[0] if self.out_size[0] else self.out_size[1]*w/h)
        out_h = float(self.out_size[1] if self.out_size[1] else self.out_size[0]*h/w)
        res = max(min(out_w, w)/w, min(out_h, h)/h)
        res_size = (int(math.floor(w*res)), int(math.floor(h*res)))
        image = image.resize(res_size, resample=Image.ANTIALIAS)
        w, h = [float(i) for i in image.size]

        if self.crop:
            x0 = int(((w - out_w) if out_w else 0)/2)
            y0 = int(((h - out_h) if out_h else 0)/2)
            image = image.crop((x0, y0, int(x0 + out_w if out_w else w), int(y0 + out_h if out_h else h)))

        try:
            image.save(self.thumbnail_filename, "PNG", quality=self.quality[0], optimize=1)
        except:
            try:
                image.save(self.thumbnail_filename, "PNG", quality=self.quality[0])
            except IOError, detail:
                raise Exception(detail)

    def get_thumbnail_url(self):
        if getattr(self, '_thumbnail_url', None) is None:
            self._thumbnail_url = "%s%s" % (
                self.store_url, os.path.basename(self.thumbnail_filename))
        return self._thumbnail_url
    thumbnail_url = property(get_thumbnail_url)

def _dummyimage(size):
    return "http://dummyimage.com/%sx%s/9e9e9e/424242.png" % size

def get_thumbnail(filename, **kwargs):
    if os.path.isfile(filename):
        try:
            thumb = Thumbnail(filename, **kwargs)
            url = thumb.thumbnail_url
        except Exception, e:
            # TODO: log error message cuz noone wishes to debug till here
            url = _dummyimage(kwargs['out_size'])
    else:
        url = _dummyimage(kwargs['out_size'])
    return url