from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user_name= models.CharField(max_length=50, unique = True, blank=False)
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length= 32, blank=True)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    clerk_user_id = models.CharField(max_length=255, blank=False)
    student_group = models.CharField(max_length=32, blank=True)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name
    
    
    
    