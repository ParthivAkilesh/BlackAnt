# Generated by Django 3.2 on 2023-07-01 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_studentinfo_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='resume',
        ),
    ]
