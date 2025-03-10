from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Student,Course,Lesson
# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    
    return render(request,"Course_app/course_list.html",{"courses":courses})

def Course_Details(request,id):
    course = get_object_or_404(Course, id=id)
    lessons = course.lesson.all()
    context ={
        'course':course,
        'lessons':lessons
    }
    
    return render(request,"Course_app/Course_details.html",context)