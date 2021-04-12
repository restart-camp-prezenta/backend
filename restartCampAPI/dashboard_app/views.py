from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions, exceptions
from rest_framework.decorators import permission_classes, authentication_classes

from .serializers import *
from .models import *


@api_view(['GET'])
def getCourses(request):
    courses = Courses.objects.all()
    serializer = CoursesSerializers(courses, many = True)
    return Response(serializer.data)