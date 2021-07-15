# Generated by Django 3.1.3 on 2021-05-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0011_auto_20210522_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='course_registered',
            field=models.ManyToManyField(blank=True, null=True, to='dashboard_app.Courses'),
        ),
        migrations.DeleteModel(
            name='LearnerSubmittedToCourses',
        ),
    ]