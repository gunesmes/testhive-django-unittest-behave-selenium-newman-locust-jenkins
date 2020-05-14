from __future__ import unicode_literals
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=60, blank=False)
    birthday = models.DateField()
    premium = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username
