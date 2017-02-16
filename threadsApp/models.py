from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


# Create your models here.

class ThreadSubject(models.Model):
    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(ThreadSubject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name


class ThreadComment(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.comment
