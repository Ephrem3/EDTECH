# Generated by Django 5.1.1 on 2024-10-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDTECH', '0002_course_teacher_alter_student_student_id_enrollment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Admin', 'Admin')], default='Teacher', max_length=10),
        ),
    ]
