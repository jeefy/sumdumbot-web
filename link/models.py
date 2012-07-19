from django.db import models

# Create your models here.

class Link(models.Model):
	url       = models.TextField()
	title     = models.TextField()
	user      = models.CharField(max_length=32)
	tags      = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	channel   = models.CharField(max_length=30)
	def __str__(self):
		return str(self.url) + ' - ' + str(self.user)

