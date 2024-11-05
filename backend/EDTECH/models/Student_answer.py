from django.db import models

# Create your models here.
class Student_answer(models.Model):
    student_answer_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=255)
    answer_grade = models.CharField(max_length=1)
    answer_stage = models.Choices('Submitted', 'Graded')
    
    
    

    
    
    def __str__(self):
        return self.user_name
    
    
    
    