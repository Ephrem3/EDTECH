from django.db import models


# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    Exam_id = models.ForeignKey('Exam', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    question_text = models.TextField(max_length=255)
    updated_at= models.DateTimeField(auto_now=True)
    

    
    
    def __str__(self):
        return self.user_name
    
    
    
    