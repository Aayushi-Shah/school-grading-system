from django.urls import path
from school import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('addmarks/<filename>',views.addMarks.as_view(),name='add_marks'),
    path('getmarks',views.getMarks.as_view(),name='get_marks'),    
    path('getmarks/<int:grade>',views.getMarksByGrade.as_view(),name='get_marks_by_grade'),
    path('getmarks/<str:subject>',views.getMarksBySubject.as_view(),name='get_marks_by_subject'),
    path('fetchmarks',views.fetchMarks.as_view(),name='fetch_marks'),
	path('fetchmarks/<int:grade>',views.fetchMarksByGrade.as_view(),name='fetch_marks_by_grade'),
    path('fetchmarks/<str:subject>',views.fetchMarksBySubject.as_view(),name='fetch_marks_by_subject'),
    path('userprofile',views.userProfile.as_view(),name='user_profile'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)