from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.courseAssign, name='course'),
    path('<int:id>/course-delete', views.courseDelete, name='courseDelete'),
    path('<int:id>/course-edit', views.courseEdit, name='courseEdit'),
    path('course-list', views.courseList, name='courseList'),
    path('<int:id>/course-detail', views.courseSingle, name='courseSingle'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
