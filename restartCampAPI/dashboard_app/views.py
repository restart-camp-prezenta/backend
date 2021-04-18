from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions, exceptions
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework import status

from .serializers import *
from .models import *

# ========================== GET and POST (Create) function for Courses =======================
@api_view(['GET', 'POST'])
def courses(request):

    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializers(courses, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoursesSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# ================== GET, UPDATE, DELETE for Course with selected PK (PK is ID) ===============
@api_view(['GET', 'PUT', 'DELETE'])
def course(request, pk):
    try:
        course = Courses.objects.get(id = pk)
    except Courses.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoursesSerializers(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoursesSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)