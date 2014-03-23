# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError
from django.conf import settings

class ImageMixin(models.Model):
    """
    mixin for models with exactly one image
    Image-Field is
    """
    image_path = 'common_storage'
    default_image = 'book_images/dummy.jpg'

    def get_image_path(self):
        return self.image_path

    def get_default_image(self):
        return self.default_image

    image_width = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Width'))

    image_height = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        verbose_name=_(u'Original Image Height'))

    image = models.ImageField(
        upload_to=get_image_path, blank=True, null=True,
        height_field='image_height',
        width_field='image_width',
            verbose_name=_(u'Original Image'))

    def _get_image(self, image_format):
        _image_format = settings.IMAGE_FORMATS[image_format]
        _img = self.image
        if not _img.name:
            _img = self.get_default_image()
        try:
            img = get_thumbnailer(_img).get_thumbnail(_image_format)
            return {
                'url': img.url,
                'width': img.width,
                'height': img.height,
                'alt': self.get_image_alt(),
                'title': self.get_image_title(),
                'format': image_format,
            }
        except (UnicodeEncodeError, InvalidImageFormatError):
            return None

    def get_image_alt(self):
        raise NotImplementedError(u'A class derived from ImageMixin ' \
            u'requires a method .get_image_alt()')

    def get_image_title(self):
        raise NotImplementedError(u'A class derived from ImageMixin ' \
            u'requires a method .get_image_title()')

    def get_image_thumb(self):
        return self._get_image('thumb')

    def get_image_main(self):
        return self._get_image('main')

    class Meta:
        abstract = True
