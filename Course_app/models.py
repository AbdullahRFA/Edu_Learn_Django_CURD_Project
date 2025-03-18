from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=25)
    descriptions = models.TextField()
    durations = models.IntegerField(help_text="Durations in hours")
    thumbnail = models.ImageField(upload_to="courses_thumbnail/", null=True, blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")  # ✅ Corrected related_name

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    email = models.EmailField(max_length=60,unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name="students")  # ✅ Changed related_name to plural

    def __str__(self):
        return self.name