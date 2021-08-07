from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CourseCategory(models.Model):
    categoryName = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Discount(models.Model):
    discountCode = models.CharField(max_length=50)
    procent = models.FloatField()
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.discountCode


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TeamRole(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateInactive = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True, upload_to ='members/')
    about = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    team = models.ForeignKey(Team, related_name='team_name', null = True, blank=True, on_delete = models.SET_NULL)
    teamRole = models.TextField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    linkedIn = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.firstName + " " + self.lastName



class Courses(models.Model):
    courseName = models.CharField(max_length = 500)
    courseSubtitle = models.CharField(max_length=300, null=True, blank=True)
    courseDescription = models.TextField(max_length=5000, null=True, blank=True)
    category = models.ForeignKey(CourseCategory, null=True, blank=True, on_delete=models.CASCADE)
    coursePrice = models.FloatField()
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    isCourseFree = models.BooleanField(default=True)
    isCourseActive = models.BooleanField(default=True)
    logo = models.ImageField(null = True, blank = True, upload_to ='logo_courses/')
    owner = models.ForeignKey(Member, null = True, blank=True, on_delete = models.SET_NULL, related_name='owner')
    trainer = models.ForeignKey(Member, null = True, blank=True, on_delete = models.SET_NULL, related_name='trainer')
    def __str__(self):
        return self.courseName


class OwnerPrc(models.Model):
    owner = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return self.owner + ' - ' + self.course


class TrainerPrc(models.Model):
    trainer = models.ForeignKey(Member, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return self.trainer + ' - ' + self.course



class Schedule(models.Model):
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField()
    courseLink = models.CharField(max_length = 100, null=True, blank=True)
    courseType = models.CharField(max_length = 100, null=True, blank=True)


    def __str__(self):
        return '{} - {}'.format(self.course, str(self.date))


class JobDomains(models.Model):
    name = models.CharField(max_length=100)
    remarks = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    name = models.CharField(max_length=100)
    remarks = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Learner(models.Model):
    REFERENCES_OPTIONS = [
        ('Facebook', 'Facebook'),
        ('LinkedIn','LinkedIn'),
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok'),
        ('De la un prieten/o ruda', 'De la un prieten/o ruda'),
        ('De la un colaborator / client', 'De la un colaborator / client'),
        ('De la managerul meu', 'De la managerul meu'),
        ('De la unul dintre angaja?ii mei', 'De la unul dintre angaja?ii mei'),
        ('Alta sursa', 'Alta sursa'),
    ] 

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    lastJob = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    remarks = models.TextField(max_length=500, null=True, blank=True)
    reference = models.CharField(max_length=30, choices=REFERENCES_OPTIONS, null=True, blank=True)
    #if is not career then is business
    is_career = models.BooleanField(default=True)
    is_business = models.BooleanField(default = False)
    has_recommended =  models.BooleanField(default = False, null=True, blank=True)
    has_participated = models.BooleanField(default = False, null=True, blank=True)
    course_registered = models.ManyToManyField(Courses, related_name='course_name')
    acord_gdpr = models.BooleanField(default=False)
    allow_newsletter = models.BooleanField(default=True)


    def __str__(self):
        return self.firstname + ' ' + self.lastname



# class LearnerSubmittedToCourses(models.Model):
#     classInfo = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
#     student = models.ForeignKey(Learner, on_delete = models.DO_NOTHING)
#     remarks_student = models.TextField(max_length=300, null=True, blank=True)
#     remarks_trainer = models.TextField(max_length=300, null=True, blank=True)



class ViewCourseScheduleTrainer(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    coursesubtitle = models.CharField(db_column='courseSubtitle', max_length=300, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    coursedescription = models.TextField(db_column='courseDescription', blank=True, null=True)  # Field name made lowercase.
    avatar = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    coursetype = models.CharField(db_column='courseType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    courselink = models.CharField(db_column='courseLink', max_length=100, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_course_schedule_trainer'    



class ViewRegistredParticipants(models.Model):
   # id = models.IntegerField(blank=True, null=False, primary_key=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    courselink = models.CharField(db_column='courseLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    days_from_register = models.FloatField(blank=True, null=True)
    weeks_to_course = models.FloatField(blank=True, null=True)
    course_week = models.FloatField(blank=True, null=True)
    participant_registration_week = models.FloatField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_registred_participants'


class ViewPrezenta(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    courses_id = models.IntegerField(blank=True, null=True)
    coursename = models.CharField(db_column='courseName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    trainerfirstname = models.CharField(db_column='trainerFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trainerlastname = models.CharField(db_column='trainerLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trainer_id = models.IntegerField(blank=True, null=True)
    learnerfirstname = models.CharField(db_column='learnerFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    learnerlastname = models.CharField(db_column='learnerLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    learnermail = models.CharField(db_column='learnerMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    learnerphone = models.CharField(db_column='learnerPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    learner_id = models.IntegerField(blank=True, null=True)
    has_participated = models.BooleanField(null=True, blank=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_prezenta'


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(null = True, blank = True, upload_to ='logo_reviews/')
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_last_name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100, null=True, blank=True)
    email = models.CharField(max_length = 100, null=True, blank=True)
    phone = models.CharField(max_length = 20, null=True, blank=True)
    message = models.TextField(max_length=1500)
    submited_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.first_last_name


class Presence(models.Model):
    participant = models.ForeignKey(Learner, on_delete = models.CASCADE)
    has_participated = models.BooleanField(default = False, null=True, blank=True)
    course = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
