# Generated by Django 3.1.3 on 2021-05-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0007_auto_20210522_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='courseLink',
        ),
        migrations.AddField(
            model_name='schedule',
            name='courseLink',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
