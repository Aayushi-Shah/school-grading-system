from django.db import models
from .encryption import *
import uuid
# Create your models here.

class User(models.Model):
	id = models.CharField(max_length=255,primary_key=True)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email = models.EmailField(max_length=255,unique=True)
	password = models.CharField(max_length=255)
	is_teacher = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.password:
			self.password = hash_password(self.password)
			self.id = uuid.uuid3(uuid.NAMESPACE_DNS, self.email)
		super(User,self).save(*args,**kwargs)

	def __str__(self):
		return self.email

	
class Marksheet(models.Model):
	grade=models.CharField(max_length=255)
	english=models.CharField(max_length=50,null=True)
	maths=models.CharField(max_length=50,null=True)
	science=models.CharField(max_length=50,null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	class Meta:
		unique_together=(("user","grade"))

	# def __str__(self):
	# 	return self.student_id