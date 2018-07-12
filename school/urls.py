from django.urls import path
from school import views

urlpatterns = [
    path('login/', views.login.as_view(), name='UserList'),
]
