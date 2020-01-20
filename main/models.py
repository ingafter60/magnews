# unicode_literals for any languages possible
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):

	name  = models.CharField(max_length=150)
	about = models.CharField(max_length=150)
	fb    = models.CharField(max_length=150)
	twt   = models.CharField(max_length=150)
	istg  = models.CharField(max_length=150)
	ytb   = models.CharField(max_length=150)
	phone = models.CharField(max_length=100)
	website  = models.CharField(max_length=150)

	set_name   = models.CharField(max_length=150)

	def __str__(self):
		# return self.name		
		return self.set_name + ' | ' + str(self.pk)