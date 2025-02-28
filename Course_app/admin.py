from django.contrib import admin
from .models import Student, Lesson, Course

# Register your models here.
class StudentModel(admin.ModelAdmin):
    list_display = ['name', 'roll', 'email', 'get_enrolled_courses']
    
    def get_enrolled_courses(self, obj):
        return ", ".join([course.title for course in obj.enrolled_courses.all()])
    
    get_enrolled_courses.short_description = "Enrolled Courses"

class LessonModel(admin.ModelAdmin):
    list_display = ['title', 'content', 'course']

class CourseModel(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'durations']

admin.site.register(Student, StudentModel)
admin.site.register(Lesson, LessonModel)
admin.site.register(Course, CourseModel)