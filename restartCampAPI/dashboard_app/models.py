from django.db import models

# Create your models here.
class CourseCategory(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name


class Discount(models.Model):
    discountCode = models.CharField(max_length=50)
    procent = models.FloatField()
    validFrom = models.DateTimeField(null=True, blank=True)
    validTo = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.discountCode


class DiscountsPacks(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    dateCreation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateInactive = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True, upload_to ='owners/')
    remarks = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    dateCreation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.DO_NOTHING)
    dateInactive = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    avatar = models.ImageField(null = True, blank = True, upload_to ='trainers/')
    remarks = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, null=True, blank=True)
    category = models.ForeignKey(CourseCategory, null=True, blank=True, on_delete=models.CASCADE)
    pret = models.FloatField()
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    free = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    logo = models.ImageField(null = True, blank = True, upload_to ='logo_courses/')
    owner = models.ForeignKey(Owner, null = True, blank=True, on_delete = models.SET_NULL)
    trainer = models.ForeignKey(Trainer, null = True, blank=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name


class OwnerPrc(models.Model):
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return self.owner + ' - ' + self.course


class TrainerPrc(models.Model):
    trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return self.trainer + ' - ' + self.course


class Schedule(models.Model):
    course = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.course + ' - ' + self.date


class JobDomains(models.Model):
    name = models.CharField(max_length=100)
    remarks = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    REFERENCES_OPTIONS = [
        ('FACEBOOK', 'FACEBOOK'),
        ('INSTAGRAM','INSTAGRAM'),
        ('LINKEDIN', 'LINKEDIN'),
        ('RECLAME INTERNET', 'RECLAME INTERNET'),
        ('RECLAME MEDIA', 'RECLAME MEDIA'),
        ('PRIETENI', 'PRIETENI'),
        ('ALTELE', 'ALTELE')
    ] 

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    lastJob = models.CharField(max_length=100, null=True, blank=True)
    domain = models.ForeignKey(JobDomains, null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    remarks = models.TextField(max_length=500, null=True, blank=True)
    reference = models.CharField(max_length=30, choices=REFERENCES_OPTIONS, null=True, blank=True)
    #if is not career then is business
    is_career = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Invoice(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    cui = models.CharField(max_length=15, null=True, blank=True)


class SoldCourses(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    discount = models.FloatField(null=True, blank=True)
    remarks = models.TextField(max_length=300, null=True, blank=True)
    invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.course + ' - ' + self.student


class Participants(models.Model):
    classInfo = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Students, on_delete = models.DO_NOTHING)
    remarks_student = models.TextField(max_length=300, null=True, blank=True)
    remarks_trainer = models.TextField(max_length=300, null=True, blank=True)


class Targets(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    money = models.FloatField(null=True, blank=True)
    participants = models.FloatField(null=True, blank=True)
    month_target = models.FloatField(null=True, blank=True)
    year_target = models.FloatField(null=True, blank=True)
    