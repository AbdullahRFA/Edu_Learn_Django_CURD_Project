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
    context = {
        'check' : 2,
        'form': form
    }

    return render(request, "Course_app/course_form.html", context)  # ✅ Pass the correct form


def course_edit(request, id):
    course = get_object_or_404(Course, id=id)  # Fetch the course object

    if request.method == "POST":
        form = courseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course details updated successfully! ✅")
            return redirect('course_list')  # Redirect after successful update
    else:
        form = courseForm(instance=course)  # Pre-fill form with course details
        
    
    context = {
        'check' : 1, 
        'course': course,
        'form': form
    }
    return render(request, "Course_app/course_form.html", context)

def course_delete(request,id):
    course = get_object_or_404(Course,id=id)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request,"Course_app/delete_course_confirmations_form.html",{'course':course})