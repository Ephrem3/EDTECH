# Generated by Django 5.1.1 on 2024-10-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDTECH', '0003_teacher_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Admin', 'Admin')], default='Teacher'),
        ),
    ]
