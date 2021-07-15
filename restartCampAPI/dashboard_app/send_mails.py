# -*- coding: latin-1 -*-
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, '/template/registration_mail.txt')
filehandle = open('/home/dev/backend/restartCampAPI/dashboard_app/template/registration_mail.txt', 'rt', encoding='latin1')
html_template = filehandle.read()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_registration_mail(html_template = html_template, courses=[], send_to='', linkuri=[]):
    text = ''
    for i,c in enumerate(courses):
        text += """<p style="margin: 0; line-height: 1.2; word-break: break-word; mso-line-height-alt: 17px; margin-top: 0; margin-bottom: 0;"><strong>{}</strong><br/>Link de acces: <a href="{}"><strong>CLICK</strong></a></p>""".format(c,linkuri[i])
    html_template = html_template.format(courses = text)
    # Define these once; use them twice!
    strFrom = "echipa.restartcamp@gmail.com"
    password = 'wjhmelljdgrvxrey'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Datele de acces - cursuri gratuite Restart Camp'
    msgRoot['From'] = strFrom
    msgRoot['To'] = send_to
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    
    msgText = MIMEText(html_template, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open("/home/dev/backend/restartCampAPI/restartCampAPI/media/mail_template/1.png", 'rb')
    msgImage1 = MIMEImage(fp.read())
    fp.close()
    msgImage1.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage1)

    fp = open("/home/dev/backend/restartCampAPI/restartCampAPI/media/mail_template/2.png", 'rb')
    msgImage2 = MIMEImage(fp.read())
    fp.close()
    msgImage2.add_header('Content-ID', '<image2>')
    msgRoot.attach(msgImage2)

    fp = open("/home/dev/backend/restartCampAPI/restartCampAPI/media/mail_template/3.png", 'rb')
    msgImage3 = MIMEImage(fp.read())
    fp.close()
    msgImage3.add_header('Content-ID', '<image3>')
    msgRoot.attach(msgImage3)

    fp = open("/home/dev/backend/restartCampAPI/restartCampAPI/media/mail_template/4.png", 'rb')
    msgImage4 = MIMEImage(fp.read())
    fp.close()
    msgImage4.add_header('Content-ID', '<image4>')
    msgRoot.attach(msgImage4)

    fp = open("/home/dev/backend/restartCampAPI/restartCampAPI/media/mail_template/5.png", 'rb')
    msgImage5 = MIMEImage(fp.read())
    fp.close()
    msgImage5.add_header('Content-ID', '<image5>')
    msgRoot.attach(msgImage5)



    # Send the email (this example assumes SMTP authentication is required)
    import smtplib, ssl


    context = ssl.create_default_context()
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls(context=context)
    smtp.login(strFrom, password)
    smtp.sendmail(strFrom, send_to, msgRoot.as_string())
    smtp.quit()


def send_contact_mail(name = '', company = '', email = '', phone = '', message = ''):
    strFrom = "echipa.restartcamp@gmail.com"
    password = 'wjhmelljdgrvxrey'
    send_to = 'echipa.restartcamp@gmail.com'
    import smtplib, ssl


    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '{} doreste sa contacteze RestartCamp'.format(name)
    msgRoot['From'] = strFrom
    msgRoot['To'] = send_to

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('{}, de la compania: {}, cu mail: {} si numar de telefon: {}, a transmis urmatorul mesaj: "{}"'.format(name, company, email, phone, message))
    msgAlternative.attach(msgText)

 

    context = ssl.create_default_context()
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls(context=context)
    smtp.login(strFrom, password)
    smtp.sendmail(strFrom, send_to, msgRoot.as_string())
    smtp.quit()


def send_weekly_mail(course_info):
    import smtplib, ssl
    from time import sleep

    strFrom = "echipa.restartcamp@gmail.com"
    password = 'wjhmelljdgrvxrey'

    context = ssl.create_default_context()
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls(context=context)
    smtp.login(strFrom, password)

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Cursurile tale pentru saptamana urmatoare'
    msgRoot['From'] = strFrom
    

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    for mail, info in course_info.items():
        msgRoot['To'] = mail
        send_to = mail
        continut = ''
        for curs in info:
            continut += 'Cursul: {} Data: {} Link: {} \n'.format(curs[0], curs[1], curs[2])
        msgText = MIMEText('{}'.format(continut))
        msgAlternative.attach(msgText)

        smtp.sendmail(strFrom, send_to, msgRoot.as_string())
        sleep(0.5)
    smtp.quit()


def send_3_days_registration_mail(mails):
    import smtplib, ssl
    from time import sleep

    strFrom = "echipa.restartcamp@gmail.com"
    password = 'wjhmelljdgrvxrey'

    context = ssl.create_default_context()
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls(context=context)
    smtp.login(strFrom, password)

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Cursurile tale pentru saptamana urmatoare'
    msgRoot['From'] = strFrom
    

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    for mail in mails:
        msgRoot['To'] = mail
        send_to = mail
        continut = 'Mesaj 3 zile'
        msgText = MIMEText('{}'.format(continut))
        msgAlternative.attach(msgText)

        smtp.sendmail(strFrom, send_to, msgRoot.as_string())
        sleep(0.5)
    smtp.quit()
