# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class employees(models.Model):
    name=models.CharField(max_length=20)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.name
# Create your models here.
