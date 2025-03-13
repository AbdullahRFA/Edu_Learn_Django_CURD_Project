from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Student,Course,Lesson
from .forms import CourseForm, LessonForm, StudentForm
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
    form = CourseForm()  # ✅ Initialize the form once

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)  # ✅ Correct form initialization
        if form.is_valid():  # ✅ Moved inside the POST check
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')  # ✅ Ensure 'course_list' is defined in `urls.py`
    context = {
        'check' : 2,
        'form': form
    }

    return render(request, "Course_app/input_and_update_form.html", context)  # ✅ Pass the correct form


def course_edit(request, id):
    course = get_object_or_404(Course, id=id)  # Fetch the course object

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course details updated successfully! ✅")
            return redirect('course_list')  # Redirect after successful update
    else:
        form = CourseForm(instance=course)  # Pre-fill form with course details
        
    
    context = {
        'check' : 1, 
        'course': course,
        'form': form
    }
    return render(request, "Course_app/input_and_update_form.html", context)

def course_delete(request,id):
    course = get_object_or_404(Course,id=id)
    if request.method == "POST":
        course.delete()
        messages.warning(request,"Course Successfully deleted!")
        return redirect('course_list')
    context = {
        'course' : course,
        'check' : 2
    }
    return render(request,"Course_app/delete_confirmation_form.html",context)




def create_lesson(request):
    form = LessonForm, StudentForm()
    if request.method == "POST":
        form = LessonForm, StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Lesson added Successfully")
            return redirect('course_list')
    context = {
        'check': 3,
        'form':form
    }
    return render(request,"Course_app/input_and_update_form.html",context)

def lesson_edit(request,id):
    lesson = get_object_or_404(Lesson,id=id)
    form = LessonForm, StudentForm(instance=lesson)
    if request.method == "POST":
        form = LessonForm, StudentForm(request.POST,request.FILES,instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request,"Lesson update Successfully")
            return redirect('course_list')
        else:
            messages.error(request,"Lesson can't update Successfully")   
    context = {
        'check' : 4,
        'form' : form
    }
    return render(request,"Course_app/input_and_update_form.html",context)


def lesson_delete(request,id):
    lesson = get_object_or_404(Lesson, id = id)
    if request.method == "POST":
        lesson.delete()
        messages.warning(request,"Lesson Successfully deleted")
        return redirect('course_list')
    context = {
        'lesson' : lesson,
        'check' : 1
        
    }
    
    return render(request,"Course_app/delete_confirmation_form.html",context)


def student_list(request):
    students = Student.objects.all()
    return render(request,"Course_app/student_list.html",{'students':students})

def Enroll_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Enrolled Successfully")
            return redirect('course_list')
    context = {
        'check' : 5,
        'form' : form
    }
    return render(request,"Course_app/input_and_update_form.html",context)

def update_student(request,id):
    student = get_object_or_404(Student,id = id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Updated Successfully")
            return redirect('course_list')
    context = {
        'check' : 6,
        'form' : form
    }
    return render(request,"Course_app/input_and_update_form.html",context)