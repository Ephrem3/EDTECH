from django.db import models


class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    Student_id = models.ForeignKey("Student", on_delete=models.CASCADE)
    Course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.Choices('Enrolled', 'Cancelled', 'pending')
    

    
    
    def __str__(self):
        return self.user_name
    
    
    
    