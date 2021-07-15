from celery.decorators import task
from celery import shared_task
from celery.utils.log import get_task_logger
from celery import Celery

from .send_mails import send_registration_mail, send_contact_mail, send_weekly_mail, send_3_days_registration_mail
from restartCampAPI.celery import app
from .models import *
import datetime

celery = Celery('tasks') #!


logger = get_task_logger(__name__)


@shared_task
def send_registrations_mail_task(courses, send_to, linkuri):
    logger.info("Sent registration mail")
    return send_registration_mail(courses = courses, send_to = send_to, linkuri = linkuri)


@shared_task
def send_contact_mail_task(name, company, email, phone, message):
    logger.info("Sent contact mail")
    return send_contact_mail(name=name, company=company, email=email, phone=phone, message=message)

@shared_task
def send_remainder_mail():
    current_week = datetime.date.today().isocalendar()[1]
    send_mails_to = {}
    participants = ViewRegistredParticipants.objects.filter(course_week = int(current_week)+1).exclude(participant_registration_week = current_week)
    mails = participants.values_list('mail', flat=True)    
    for mail in mails:
        if mail not in send_mails_to:
            cursuri = participants.filter(mail=mail).values_list('coursename', flat=True)
            data_cursuri = participants.filter(mail=mail).values_list('date', flat=True)
            linkuri = participants.filter(mail=mail).values_list('courselink', flat=True)
            curs_link = list(set(list(zip(cursuri, data_cursuri, linkuri))))
            send_mails_to[mail] = curs_link

    logger.info("Sent weekly mail")
    logger.info(send_mails_to)
    return send_weekly_mail (send_mails_to)   


@shared_task
def send_3_days_registration_mail_task():
    ago_3_days = datetime.date.today() - datetime.timedelta(days=3)
    participants = Learner.objects.filter(created_on__day = ago_3_days.day, created_on__month = ago_3_days.month,created_on__year = ago_3_days.year)
    mails = participants.values_list('mail', flat=True).distinct()
    logger.info("Sent 3 days mail")
    return send_3_days_registration_mail(mails) 


