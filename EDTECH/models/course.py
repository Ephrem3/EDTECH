from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name= models.CharField(max_length=50, blank=False)
    course_code= models.CharField(max_length=12, blank=False)
    course_description= models.TextField(max_length=255, blank=True)
    capacity = models.IntegerField(blank=False)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user_name
    
    
    
    