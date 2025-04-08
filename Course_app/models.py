from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=25)
    descriptions = models.TextField()
    durations = models.IntegerField(help_text="Durations in hours")
    thumbnail = models.ImageField(upload_to="courses_thumbnail/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")  # ✅ Corrected related_name
    video_URL = models.URLField(null=True,blank=True)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    email = models.EmailField(max_length=60,unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name="students")  # ✅ Changed related_name to plural
    completed_lesson = models.ManyToManyField(Lesson,related_name='completed_by',blank=True)

    def __str__(self):
        return self.name