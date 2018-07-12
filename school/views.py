from django.shortcuts import render
from django.http import *
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import sys
from . import permissions
from .encryption import *
class login(APIView):
	# permission_classes = (IsAuthenticatedOrReadOnly,)
	def post(self, request, format=None):
		print(request.data)
		email=request.data['email']
		password=request.data['password']
		try:
			u = User.objects.get(email=email)
			success=check_password(u.password,password)
			message = ""
			if success:
				message="Logged in Successfully"
			else:
				message = "Invalid Credentials"
			return JsonResponse({"success":success,"message":message})
		except User.DoesNotExist:
			success = False
			message = "Invalid Credentials"
			return HttpResponseForbidden({"success":success,"message":message}, content_type="application/json")
		

