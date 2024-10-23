from django.db import models

# Create your models here.
class Answer(models.Model):
    
    answer_id = models.AutoField(primary_key=True)
    answer_text = models.TextField(max_length=255)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    
    def __str__(self):
        return self.user_name
    
    
    
    