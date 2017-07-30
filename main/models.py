# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=5000)
	is_activity = models.BooleanField(default=False)
	date_created = models.DateTimeField('date published', default=timezone.now())

	def __str__(self):
		return self.title