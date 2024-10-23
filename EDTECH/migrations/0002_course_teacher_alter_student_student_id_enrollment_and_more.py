# Generated by Django 5.1.1 on 2024-10-09 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDTECH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=12)),
                ('course_description', models.TextField(blank=True, max_length=255)),
                ('capacity', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('clerk_user_id', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('Course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.course')),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.student')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_id', models.CharField(max_length=100)),
                ('exam_name', models.CharField(max_length=100)),
                ('exam_description', models.TextField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('End_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question_text', models.TextField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.question')),
            ],
        ),
        migrations.CreateModel(
            name='Student_answer',
            fields=[
                ('student_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField(max_length=255)),
                ('answer_grade', models.CharField(max_length=1)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EDTECH.teacher'),
        ),
    ]