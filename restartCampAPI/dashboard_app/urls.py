from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('contact', views.contact, name = 'contact'),
    path('courses', views.courses, name = 'courses'),
    path('course/<str:pk>', views.course, name = 'course'),
    path('course_schedule_trainer_all', views.course_schedule_trainer_all, name = 'course_schedule_trainer_all'),
    path('course_schedule_trainer/<str:pk>', views.course_schedule_trainer, name = 'course_schedule_trainer'),
    path('members', views.members, name = 'members'),
    path('learner', views.learner, name = 'learner'),
    path('learner_detail/<str:pk>', views.learner_detail, name = 'learner_detail'),
    path('testimonials', views.testimonials, name = 'testimonials'),
    path('presence/<str:pk>/<str:pk2>', views.presence, name = 'presence'),
    url(r'^authenticate', views.CustomObtainAuthToken.as_view()),
    path('participant_presence/<str:pk>/<str:pk2>', views.participant_presence, name = 'participant_presence'),
   # path('auth', include('djoser.urls.authtoken'))
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)