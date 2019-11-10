# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User



@python_2_unicode_compatible
class BroadcastMessages(models.Model):
    broadcast_type = models.CharField(max_length=10, blank=True, null=True)
    broadcast_message = models.CharField(max_length=500, default='Enter a single line summary')
    group_role = models.CharField(max_length=10, blank=True, null=True)
    claim = models.BooleanField(default=False)
    claim_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    br_params = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.broadcast_message
