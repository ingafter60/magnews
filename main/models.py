# unicode_literals for any languages possible
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):

	name  = models.TextField()
	about = models.TextField(null=True)
	fb    = models.TextField(default='-')
	twt   = models.TextField(default='-')
	istg  = models.TextField(default='-')
	ytb   = models.TextField(default='-')

	set_name   = models.TextField(default='-')

	def __str__(self):
		# return self.name		
		return self.set_name + ' | ' + str(self.pk)