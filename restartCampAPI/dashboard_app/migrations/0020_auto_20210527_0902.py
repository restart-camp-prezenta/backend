# Generated by Django 3.1.3 on 2021-05-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0019_viewcoursescheduletrainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='remarks',
            new_name='about',
        ),
        migrations.AlterField(
            model_name='member',
            name='teamRole',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]