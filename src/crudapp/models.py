from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	address = models.CharField(max_length=100, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name