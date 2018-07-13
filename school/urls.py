from django.urls import path
from school import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('addmarks/<filename>',views.addMarks.as_view(),name='add_marks'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)