#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import permalink

from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError

from bases.image import BaseImage
from imagestore.utils import load_class, get_model_string

class Image(BaseImage):
    class Meta(BaseImage.Meta):
        abstract = False
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        app_label = 'imagestore'

    @permalink
    def get_absolute_url(self):
        return 'imagestore:image', (), {'pk': self.id}

    def get_api_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)

    def get_sm_img_url(self):
        try:
            return get_thumbnail(self.image, '200x150', crop='center').url
        except IOError:
            return 'IOError'
        except ThumbnailError, ex:
            return 'ThumbnailError, %s' % ex.message

    def get_md_img_url(self):
        try:
            return get_thumbnail(self.image, '320x240', crop='center').url
        except IOError:
            return 'IOError'
        except ThumbnailError, ex:
            return 'ThumbnailError, %s' % ex.message

    def get_lg_img_url(self):
        try:
            return get_thumbnail(self.image, '400x300', crop='center').url
        except IOError:
            return 'IOError'
        except ThumbnailError, ex:
            return 'ThumbnailError, %s' % ex.message
