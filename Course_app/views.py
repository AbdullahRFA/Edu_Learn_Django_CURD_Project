from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Student,Course,Lesson
from .forms import courseForm, lessonForm
from django.contrib import messages
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


def create_course(request):
    form = courseForm()  # ✅ Initialize the form once

    if request.method == "POST":
        form = courseForm(request.POST, request.FILES)  # ✅ Correct form initialization
        if form.is_valid():  # ✅ Moved inside the POST check
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')  # ✅ Ensure 'course_list' is defined in `urls.py`

    return render(request, "Course_app/course_form.html", {'form': form})  # ✅ Pass the correct form


def course_edit(request,id):
    return HttpResponse("This is course_edit")
def course_delete(request,id):
    return HttpResponse("This is course_delete")