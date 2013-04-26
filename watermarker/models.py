# -*- coding: utf-8 -*-

from django.db import models

class Watermark(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'Название')
    image = models.ImageField(upload_to='watermarks', verbose_name=u'Изображение')
    is_active = models.BooleanField(default=True, blank=True, verbose_name=u'Активность')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']