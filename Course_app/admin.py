from django.contrib import admin
from .models import Student, Lesson, Course

# Register your models here.
class StudentModel(admin.ModelAdmin):
    list_display = ['name', 'roll', 'email', 'get_enrolled_courses','get_completed_lesson']
    
    def get_enrolled_courses(self, obj):
        return ", ".join([course.title for course in obj.enrolled_courses.all()])
    
    get_enrolled_courses.short_description = "Enrolled Courses"
    
    def get_completed_lesson(self,obj):
        return ", ".join([lesson.title for lesson in obj.completed_lesson.all()])
    get_completed_lesson.short_description = "Completed Lessons"

class LessonModel(admin.ModelAdmin):
    list_display = ['title', 'content', 'course','video_URL','completion_status']

class CourseModel(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'durations','created_at']

admin.site.register(Student, StudentModel)
admin.site.register(Lesson, LessonModel)
admin.site.register(Course, CourseModel)