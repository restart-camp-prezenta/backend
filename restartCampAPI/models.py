# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ViewCourseScheduleTrainer(models.Model):
    id = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    coursesubtitle = models.CharField(db_column='courseSubtitle', max_length=300, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    coursedescription = models.TextField(db_column='courseDescription', blank=True, null=True)  # Field name made lowercase.
    avatar = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    coursetype = models.CharField(db_column='courseType', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_course_schedule_trainer'
