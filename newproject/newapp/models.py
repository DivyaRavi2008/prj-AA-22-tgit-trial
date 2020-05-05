# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    dob = models.DateField()
    moto = models.TextField()

    class Meta:
        db_table = 'team'

