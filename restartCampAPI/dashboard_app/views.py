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

import smtplib, ssl


# =================================== Variables for mails =====================================
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "send.automated.mails@gmail.com"
password = 'AutomatedMails'


# ========================== GET and POST (Create) function for Courses =======================
@api_view(['GET', 'POST'])
def courses(request):

    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializers(courses, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoursesSerializers(data = request.data)
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



# ========================== GET and POST (Create) function for Team/Members =======================
@api_view(['GET', 'POST'])
def members(request):

    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializers(members, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# ========================== POST (Create) function for REGISTRAIONS =======================
@api_view(['GET', 'POST'])
def learner(request):

    if request.method == 'GET':
        learners = Learner.objects.all()
        serializer = LearnerSerializers(learners, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        print(data)
        new_student = Learner.objects.create(
            firstname = data['firstname'],
            lastname = data['lastname'],
            phone = data['phone'],
            mail = data['mail'],
            lastJob = data['lastJob'],
            job = data['job'],
            remarks = data['remarks'],
            reference = data['reference'],
            is_career = data['is_career'],
            is_business = data['is_business'],
            domain = data['domain'],
        )
        new_student.save()

        registered_courses = '\nAi fost inregistrat cu succes la urmatoarele cursuri: \n'
        print('---------------------------------------------')
        print(data['course_registered'])
        for course in data['course_registered']:
            registered_courses += course
            registered_courses += '\n'
            course_obj = Courses.objects.get(courseName = course)
            new_student.course_registered.add(course_obj)

        serializer = LearnerSerializers(new_student)
        
        receiver_email = data['mail']
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                message = u'{}'.format(registered_courses)
                message = message.encode("utf-8")
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                print(message)
                server.quit()
        except Exception as e:
            print(e)
    
                
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


 # ============ GET function for ViewCourseScheduleTrainer with selected PK (PK is ID) ==============
@api_view(['GET', 'POST'])
def course_schedule_trainer(request, pk):
    try:
        course_schedule_trainer = ViewCourseScheduleTrainer.objects.get(id = pk)
    except ViewCourseScheduleTrainer.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = ViewCourseScheduleTrainerSerializers(course_schedule_trainer)
        return Response(serializer.data)


 # ========================== GET function for ViewCourseScheduleTrainer  =======================
@api_view(['GET', 'POST'])
def course_schedule_trainer_all(request):   
    if request.method == 'GET':
        course_schedule_trainer = ViewCourseScheduleTrainer.objects.all()
        serializer = ViewCourseScheduleTrainerSerializers(course_schedule_trainer, many = True)
        return Response(serializer.data)
       


 # ========================== GET function for Testimonials  =======================
@api_view(['GET', 'POST'])
def testimonials(request):   
    if request.method == 'GET':
        testimonials = Testimonials.objects.all()
        serializer = TestimonialsSerializers(testimonials, many = True)
        return Response(serializer.data)

       