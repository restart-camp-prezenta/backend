# Generated by Django 3.1.3 on 2021-05-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0020_auto_20210527_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
