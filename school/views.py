#importing Djando modules
import sys
from django.shortcuts import render
from django.http import *

#Importing rest_framework modules
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.parsers import *
from rest_framework import status

#Importing models and serializers modules
from .models import *
from .serializers import *

#Importing user defined modules
from .encryption import *
from .pdfconvertor import *

SUBJECT_LIST = ["english","maths","science"] #List for subjects in the Marksheet model

# Error Messages
INVALID_STUDENT_MESSAGE = "Students in invalid_student_list DoesNotExist!!!" 
MARKS_ALREADY_EXISTS_MESSAGE = "Marks have already been entered for students in failure_list"
UNAUTHORIZED_MESSAGE = "You're not authorized!!!"
INVALID_SUBJECT_MESSAGE = "Subject Not Available"
EMPTY_MARKSHEET_MESSAGE = "Marksheet Not Available"

# ClassBasedView for login 
class login(APIView):
	def post(self, request, format=None):
		"""

		"""
		email=request.data['email']
		password=request.data['password']
		data = {}
		try:
			u = User.objects.get(email=email)
			success=check_password(u.password,password)
			if success:
				data['success'] = success
				data['message']="Logged in Successfully"
				data['id'] = u.id
				return Response(data)
			else:
				raise User.DoesNotExist
		except User.DoesNotExist:
			data['success'] = False
			data['message'] = "Invalid Credentials"			
			return Response(data,status=403)

class addMarks(APIView):
	"""docstring for AddMarks"""
	parser_classes = (FileUploadParser,)
	def post(self, request, filename, format=None):
		id = request.META['HTTP_TOKEN']
		try:
			u = User.objects.get(id=id,is_teacher=True)
			f = request.data['file']
			with open('input.pdf', 'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
				data=convert('input.pdf')
			
			marksheet=Marksheet()
			row_count=data.shape[0]
			success_list = []
			failure_list = []
			invalid_student_list = []
			messages = []
			for row in range(row_count):
				student_id=data.iloc[row]['student_id']
				try:
					print("Student\t\t:{0}".format(student_id))
					user = User.objects.get(email=student_id,is_teacher=False)
					grade=data.iloc[row]['grade']
					english=data.iloc[row]['english']
					maths=data.iloc[row]['maths']
					science=data.iloc[row]['science']
					Marksheet.objects.create(user=user, grade=grade, english=english,maths=maths,science=science)
				except User.DoesNotExist:
					invalid_student_list.append(student_id)
					if INVALID_STUDENT_MESSAGE not in messages:
						messages.append(INVALID_STUDENT_MESSAGE)
					continue
				except:
					failure_list.append(student_id)
					if MARKS_ALREADY_EXISTS_MESSAGE not in messages:
						messages.append(MARKS_ALREADY_EXISTS_MESSAGE)					
					continue
				success_list.append(student_id)
			data = {}
			data['messages'] = messages
			data['student_list'] = success_list
			data['invalid_student_list'] = invalid_student_list
			data['failure_list'] = failure_list
			if success_list:
				data['success'] = True
				data['marks_entered_by'] = u.email
				return Response(data)
			else:
				data['success'] = False	
				return Response(data, status = 422)
		except Exception as e:
			data = {}
			data['success'] = False
			data['message'] = UNAUTHORIZED_MESSAGE
			return Response(data,status=403)

#ClassBasedView for getting marks for student
class getMarks(APIView):
	def get(self, request, format=None):
		id = request.META['HTTP_TOKEN']
		data = {}
		try:
			u = User.objects.get(id=id,is_teacher=False)
			marks = Marksheet.objects.filter(user = u)
			return studentMarksJSON(marks,u)
		except Exception:
			data['success'] = False
			data['message'] = UNAUTHORIZED_MESSAGE
			return Response(data,status=403)

#ClassBasedView for getting marks by grade for student
class getMarksByGrade(APIView):
	def get(self, request, grade, format=None):
		id = request.META['HTTP_TOKEN']
		data = {}
		try:
			u = User.objects.get(id=id,is_teacher=False)
			marks = Marksheet.objects.filter(user = u, grade = grade)
			return studentMarksJSON(marks,u)
		except Exception:
			data['success'] = False
			data['message'] = UNAUTHORIZED_MESSAGE
			return Response(data,status=403)

#ClassBasedView for getting marks by subject for student
class getMarksBySubject(APIView):
	def get(self, request, subject, format=None):
		data = {}
		id = request.META['HTTP_TOKEN']
		try:
			if subject not in SUBJECT_LIST:
				data['message'] = INVALID_SUBJECT_MESSAGE
				data['success'] = False
				return Response(data,status=422)
			else:
				u = User.objects.get(id=id,is_teacher=False)
				marks = Marksheet.objects.filter(user = u)
				if marks:
						data['success'] = True
						serialized_data = MarksStudentSerializer(marks,many=True).data
						new_data = []
						for i in serialized_data:
							new_data.append(dict(i))
						for d in new_data:
							l = list(d.keys())
							for key in l:
								if key not in ["grade",subject]:
									del d[key]
						data['data'] = new_data								
						data['message'] = "Marks fetched for {0}".format(u.email)
						return Response(data)
				else:
					data['message'] = EMPTY_MARKSHEET_MESSAGE
					data['success'] = False
					return Response(data,status=422)
		except Exception:
			data['success'] = False
			data['message'] = UNAUTHORIZED_MESSAGE
			return Response(data,status=403)

#ClassBasedView for fetching marks for teacher
class fetchMarks(APIView):
	def get(self, request, format=None):
		id = request.META['HTTP_TOKEN']
		try:
			u = User.objects.get(id=id,is_teacher=True)
			# Logic HERE 
			marks = Marksheet.objects.all()
			return teacherMarksJSON(marks,u)
		except User.DoesNotExist:
			data = {}
			data['success'] = False
			data['message'] = UNAUTHORIZED_MESSAGE
			return Response(data,status=403)



def studentMarksJSON(marks,u):
	data = {}
	if marks:
		data['success'] = True
		data['data'] = MarksStudentSerializer(marks,many=True).data
		data['message'] = "Marks fetched for {0}".format(u.email)
		return Response(data)
	else:
		data['message'] = EMPTY_MARKSHEET_MESSAGE
		data['success'] = False
		return Response(data,status=422)

def teacherMarksJSON(marks,u):
	data = {}	
	if marks:
		data['success'] = True					
		serialized_data = MarksTeacherSerializer(marks,many=True).data
		for d in serialized_data:			
			d['student'] = User.objects.get(id=d["user"],is_teacher=False).email
			del d["user"]
		data['data'] = serialized_data
		data['message'] = "Marks fetched for {0}".format(u.email)
		return Response(data)
	else:
		data['message'] = EMPTY_MARKSHEET_MESSAGE
		data['success'] = False
		return Response(data,status=422)



