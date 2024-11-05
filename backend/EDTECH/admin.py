from django.contrib import admin


from .models import Question
admin.site.register(Question)
from .models import Answer
admin.site.register(Answer)
from .models import Exam
admin.site.register(Exam)
from .models import Course
admin.site.register(Course)
from .models import Enrollment
admin.site.register(Enrollment)
from .models import Student
admin.site.register(Student)
from .models import Teacher
admin.site.register(Teacher)
from .models import Student_answer
admin.site.register(Student_answer)

    