from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('courses', views.courses, name = 'courses'),
    path('course/<str:pk>', views.course, name = 'course'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)