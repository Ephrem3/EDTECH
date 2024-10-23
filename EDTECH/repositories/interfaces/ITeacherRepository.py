from abc import ABC, abstractmethod

class ITeacherRepository(ABC):
    @abstractmethod
    def get_all_teachers(self):
        pass

    @abstractmethod
    def get_teacher_by_user_name(self, user_name):
        pass

    @abstractmethod
    def add_teacher(self, teacher):
        pass

    @abstractmethod
    def update_teacher(self, teacher):
        pass

    @abstractmethod
    def delete_teacher(self, teacher_id):
        pass

    @abstractmethod
    def get_teacher_by_email(self, email):
        pass
    
    def get_teacher_by_id(self, teacher_id):
        pass
    
    
