from ACM_SIGAI.EDTECH.models import teacher
from ACM_SIGAI.EDTECH.repositories.interfaces import ITeacherRepository

class teacherRepository(ITeacherRepository):
    def get_all_teachers(self):
        return teacher.objects.filter(is_active=True)

    def get_teacher_by_user_name(self, user_name):
        return teacher.objects.get(user_name=user_name)
    
    def get_teacher_by_email(self, email):
        return teacher.objects.get(email=email)
    
    def add_teacher(self, teacher):
        teacher = teacher(**teacher)
        teacher.save()
        return teacher
    
    def update_teacher(self, teacher):
        teacher.save()
        return teacher
    
    def delete_teacher(self, teacher_id):
        teacher = teacher.objects.get(teacher_id=teacher_id)
        teacher.is_active = False
        teacher.save()
        return teacher

    def get_teacher_by_id(self, teacher_id):
        return teacher.objects.get(teacher_id=teacher_id)
    