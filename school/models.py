from django.db import models
from .encryption import *
# Create your models here.

class User(models.Model):
	email = models.EmailField(max_length=255,unique=True)
	password = models.CharField(max_length=255)
	is_teacher = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.password:
			self.password = hash_password(self.password)
		super(User,self).save(*args,**kwargs)

	def __str__(self):
		return self.email


