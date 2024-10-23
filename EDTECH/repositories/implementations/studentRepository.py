

from ACM_SIGAI.EDTECH.models import student
from ACM_SIGAI.EDTECH.repositories.interfaces import IStudentRepository


class studentRepository(IStudentRepository):
    def add_student(self, student):
        student = student(**student)
        student.save()
        return student
    
    def get_sudent_by_user_name(self, user_name):
        return student.objects.get(user_name=user_name)
    
    def get_student_by_email(self,email):
        return student.objects.get (email=email)
    
    def update_student(self,student):
        student.save()
        return student
    
    def delete_student(self,student_id):
        student = student.objects.get(student_id=student_id)
        student.is_active = False
        student.save()
        return student
    
    def get_all_students(self):
        return student.objects.filter(is_active=True)
    
    def get_student_by_id(self, student_id):
        return student.objects.get(student_id=student_id)

    
    
    
    
    
        
        
        
    
    
    
    