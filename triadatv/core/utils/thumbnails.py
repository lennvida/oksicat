# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageEnhance
import math
import os.path
import sys

from django.conf import settings

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

METHOD_LIST = ('crop', 'expand', 'autocrop', 'upscale', 'bw', 'detail', 'sharpen', 'desaturate')

class Thumbnail(object):

    quality = 98
    size = (150, 150)

    crop, expand, autocrop, upscale = False, False, False, False
    bw, detail, sharpen = False, False, False

    store_dir = settings.THUMBNAIL_DIR
    store_url = settings.THUMBNAIL_URL

    hash_attr_list = ('filename', 'size', 'quality') + METHOD_LIST

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

    def get_hash(self):
        hash = []
        for attr in self.hash_attr_list:
            hash.append(getattr(self, attr, False))
        return md5(unicode(hash)).hexdigest()

    def get_thumbnail_url(self):
        if getattr(self, '_thumbnail_url', None) is None:
            self._thumbnail_url = "%s%s" % (
                self.store_url, os.path.basename(self.thumbnail_filename))
        return self._thumbnail_url
    thumbnail_url = property(get_thumbnail_url)

    def get_thumbnail_filename(self):
        if getattr(self, '_thumbnail_filename', None) is None:
            filename = '%s.jpg' % self.get_hash()
            if not os.path.exists(self.store_dir):
                os.mkdir(self.store_dir)
            self._thumbnail_filename = os.path.join(self.store_dir, filename)
        return self._thumbnail_filename
    thumbnail_filename = property(get_thumbnail_filename)

    def make_thumbnail(self):
        try:
            image = Image.open(self.filename)
        except IOError, detail:
            raise Exception(detail)

        if getattr(self, 'bw', False):
            image = image.convert("L")
        elif image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        if getattr(self, 'autocrop', False):
            image = autocrop(image)

        x, y   = [float(v) for v in image.size]
        xr, yr = [float(v) for v in self.size]

        if getattr(self, 'crop', False):
            res = max(xr/x, yr/y)
        else:
            res = min(xr/x, yr/y)

        if not getattr(self, 'upscale', False):
            res = min(res, 1)

        xnew, ynew = int(math.floor(x*res)), int(math.floor(y*res))
        image = image.resize((xnew, ynew), resample=Image.ANTIALIAS)
        
        if getattr(self, 'expand', False):
            insimage = image
            dx, dy = (xr-xnew)/2, (yr-ynew)/2
            image = Image.new("RGB", (int(xr), int(yr)), getattr(self, 'expand_color', "#ffffff"))
            image.paste(insimage, (int(dx), int(dy), int(dx+xnew), int(dy+ynew)))

        if getattr(self, 'crop', False):
            x, y   = [float(v) for v in image.size]
            ex, ey = (x-min(x, xr))/2, (y-min(y, yr))/2
            image = image.crop((int(ex), int(ey), int(x-ex), int(y-ey)))

        if getattr(self, 'detail', False):
            image = image.filter(ImageFilter.DETAIL)

        if getattr(self, 'sharpen', False):
            sharpener = ImageEnhance.Sharpness(image)
            image = sharpener.enhance(getattr(self, 'sharpen_value', 1))

        if getattr(self, 'desaturate', False):
            image = ImageEnhance.Color(image).enhance(0.0)

        try:
            image.save(self.thumbnail_filename, "JPEG", quality=self.quality, optimize=1)
        except:
            try:
                image.save(self.thumbnail_filename, "JPEG", quality=self.quality)
            except IOError, detail:
                raise Exception(detail)

def autocrop(image):

    WHITE_RATIO = 0.95

    bw = image.convert("1")
    pix = bw.load()

    x0, x1, y0, y1 = 0, image.size[0], 0, image.size[1]

    def col_is_white(x):
        s = 0.0
        for i in xrange(0,image.size[1]):
            s += pix[x,i]/255
        return s/float(image.size[1]) > WHITE_RATIO

    def row_is_white(y):
        s = 0.0
        for i in xrange(0,image.size[0]):
            s += pix[i,y]/255
        return s/float(image.size[0]) > WHITE_RATIO

    for i in xrange(0,image.size[0]):
        if not col_is_white(i):
            x0 = i
            break

    for i in xrange(0,image.size[1]):
        if not row_is_white(i):
            y0 = i
            break

    for i in xrange(image.size[0]-1, -1, -1):
        if not col_is_white(i):
            x1 = i+1
            break

    for i in xrange(image.size[1]-1, -1, -1):
        if not row_is_white(i):
            y1 = i+1
            break

    return image.crop((x0, y0, x1, y1))

def _placehold(size):
    return "http://placehold.it/%sx%s" % size

def get_thumbnail(filename, **kwargs):
    if os.path.isfile(filename):
        try:
            thumb = Thumbnail(filename, **kwargs)
            url = thumb.thumbnail_url
        except Exception, e:
            #TODO: log error message cuz noone wishes to debug till here
            url = _placehold(kwargs['size'])
    else:
        url = _placehold(kwargs['size'])
    return url