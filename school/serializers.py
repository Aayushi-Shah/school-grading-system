from rest_framework import serializers
from .models import *

class MarksStudentSerializer (serializers.ModelSerializer):
 	class Meta:
 		model = Marksheet
 		exclude = ('id','user',)

class MarksTeacherSerializer (serializers.ModelSerializer):
 	class Meta:
 		model = Marksheet
 		exclude = ('id',)

class UserSerializer (serializers.ModelSerializer):
 	class Meta:
 		model = User
 		exclude = ('id','password')
