from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions, exceptions
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *
from .send_mails import send_registration_mail, send_contact_mail

from .tasks import send_registrations_mail_task, send_contact_mail_task
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.generator import Generator
from email.mime.text import MIMEText
import datetime

# =================================== Variables for mails =====================================
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "echipa.restartcamp@gmail.com"
password = 'wjhmelljdgrvxrey'
EMAIL_ADDRESS = sender_email
EMAIL_PASSWORD = password 

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
        cursuri_all = ViewCourseScheduleTrainer.objects.all()
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

        registered_courses = []
        linkuri = []
        for course in data['course_registered']:
            linkuri.append(cursuri_all.get(coursename = course).courselink)
            registered_courses.append(course)
            course_obj = Courses.objects.get(courseName = course)
            new_student.course_registered.add(course_obj)

        serializer = LearnerSerializers(new_student)
        
        receiver_email = data['mail']
        try:
            send_registrations_mail_task.delay(courses = registered_courses, send_to = receiver_email, linkuri = linkuri)
        except Exception as e:
            print(e)
    
                
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# ================== GET, UPDATE, DELETE for Course with selected PK (PK is ID) ===============
@api_view(['GET', 'PUT', 'DELETE'])
def learner_detail(request, pk):
    try:
        learner = Learner.objects.get(id = pk)
    except Learner.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LearnerSerializers(learner)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LearnerSerializers(learner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'DELETE':
        learner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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



# ========================== GET function for Contact =======================
@api_view(['GET', 'POST'])
def contact(request):

    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializers(contact , many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        contact_name = data['first_last_name']
        contact_company = data['company']
        contact_email = data['email']
        contact_phone = data['phone']
        contact_message = data['message']

        serializer = ContactSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_contact_mail_task.delay(name=contact_name, company=contact_company, email=contact_email, phone=contact_phone, message=contact_message)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# ========================== GET function for Presence =======================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def presence(request, pk, pk2):
    try:
        prezenta = ViewPrezenta.objects.filter(trainer_id = pk, courses_id = pk2)
    except Learner.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = ViewPrezentaSerializers(prezenta , many = True)
        return Response(serializer.data)


# ========================== Participants presence ===========================
@api_view(['POST'])
def participant_presence(request, pk, pk2):
    course_id = pk2
    learner_id = pk
    if request.method == 'POST':
        if ViewPrezenta.objects.filter(learner_id = pk, courses_id = pk2).count()>0:
            serializer = PresenceSerializers(data = request.data)
            if serializer.is_valid():
                if Presence.objects.filter(participant_id = pk, course_id = pk2).count()>0:
                    new_data = serializer.data
                    new_data['link'] = Schedule.objects.get(course = pk2).courseLink
                    return Response(new_data, status = status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    new_data = serializer.data
                    new_data['link'] = Schedule.objects.get(course = pk2).courseLink
                    return Response(new_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# =========================== LOGIN and obtain TOKEN =========================
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        trainer = Member.objects.get(user = token.user_id).id
        today = datetime.date.today()
        try:
            trainer_schedule = Schedule.objects.filter(course__trainer = trainer).order_by('date')
            trainer_schedule_today = trainer_schedule.filter(date__month=today.month, date__day = today.day, date__year = today.year)
            if trainer_schedule_today.count()>0:
                course_id = trainer_schedule_today[0].course_id
            else:
                course_id = trainer_schedule[0].course_id
        except Exception as e:
            print(e)
            course_id = 0
        return Response({'token': token.key, 'id': token.user_id, 'trainer_id':trainer, 'course_id':course_id})