from rest_framework import permissions
from .models import User

class TeacherAccessPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		email=request.data.email
		return User.objects.get(email=email).is_teacher

		
class StudentAccessPermission(permissions.BasePermission):
	def has_permission(self, request, view):
		email=request.data.email
		return not User.objects.get(email=email).is_teacher
