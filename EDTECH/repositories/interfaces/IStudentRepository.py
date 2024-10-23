from abc import ABC, abstractmethod
from typing import List, Optional


class IStudentRepository(ABC):
    @abstractmethod
    def get_all_students(self):
        pass
    @abstractmethod
    def get_student_by_user_name(self, user_name):
        pass

    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def update_student(self, student):
        pass

    @abstractmethod
    def delete_student(self, student_id):
        pass

    @abstractmethod
    def get_student_by_email(self, email):
        pass

    def get_student_by_id(self, student_id):
        pass
    
    