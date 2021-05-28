from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('courses', views.courses, name = 'courses'),
    path('course/<str:pk>', views.course, name = 'course'),
    path('course_schedule_trainer_all', views.course_schedule_trainer_all, name = 'course_schedule_trainer_all'),
    path('course_schedule_trainer/<str:pk>', views.course_schedule_trainer, name = 'course_schedule_trainer'),
    path('members', views.members, name = 'members'),
    path('learner', views.learner, name = 'learner'),
    path('testimonials', views.testimonials, name = 'testimonials'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)