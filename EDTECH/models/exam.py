from django.db import models

class Exam(models.Model):
    Exam_id = models.CharField(max_length=100)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    exam_name =models.CharField(max_length=100)
    exam_description = models.TextField(max_length=255)
    start_date = models.DateTimeField(auto_now = False)
    End_date = models.DateTimeField(auto_now = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.user_name
    
    
    
    
    
    