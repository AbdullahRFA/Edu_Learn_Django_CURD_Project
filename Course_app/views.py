from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm, LessonForm, StudentForm, UserRegistrationForm
from .models import Course, Lesson, Student

# html_path_variabl
html_path_delete_confirmation_form = "Course_app/delete_confirmation_form.html"
html_path_for_student_list="Course_app/student_list.html"
html_path_for_input_and_update="Course_app/input_and_update_form.html"

# Create your views here.
@login_required(login_url='login_user')
def course_list(request):
    courses = Course.objects.all()
    
    return render(request,"Course_app/course_list.html",{"courses":courses})

@login_required(login_url='login_user')
def Course_Details(request,id):
    course = get_object_or_404(Course, id=id)
    lessons = course.lessons.all()
    context ={
        'course':course,
        'lessons':lessons
    }
    
    return render(request,"Course_app/Course_details.html",context)

@login_required(login_url='login_user')
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


    return render(request, html_path_for_input_and_update, context)  # ✅ Pass the correct form


@login_required(login_url='login_user')
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
    return render(request, html_path_for_input_and_update, context)

@login_required(login_url='login_user')
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
    return render(request,html_path_delete_confirmation_form,context)



@login_required(login_url='login_user')
def create_lesson(request):
    form = LessonForm()
    if request.method == "POST":
        form = LessonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Lesson added Successfully")
            return redirect('course_list')
    context = {
        'check': 3,
        'form':form
    }
    return render(request,html_path_for_input_and_update,context)

@login_required(login_url='login_user')
def lesson_edit(request,id):
    lesson = get_object_or_404(Lesson,id=id)
    form = LessonForm(instance=lesson)
    if request.method == "POST":
        form = LessonForm(request.POST,request.FILES,instance=lesson)
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
    return render(request,html_path_for_input_and_update,context)


@login_required(login_url='login_user')
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
    
    return render(request,html_path_delete_confirmation_form,context)

@login_required(login_url='login_user')
def student_list(request):
    students = Student.objects.all()
    context = {
        'check':1,
        'students':students
    }
    return render(request,html_path_for_student_list,context)

@login_required(login_url='login_user')
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
    return render(request,html_path_for_input_and_update,context)

@login_required(login_url='login_user')
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
    return render(request,html_path_for_input_and_update,context)

@login_required(login_url='login_user')
def delete_student(request,id):
    student = get_object_or_404(Student,id = id)
    if request.method == "POST":
        student.delete()
        messages.warning(request,"Student Deleted Successfully")
        return redirect('student_list')
    context = {
        'check' : 3,
        'student' : student
    }
    return render(request,html_path_delete_confirmation_form,context)


@login_required(login_url='login_user')
def individual_course_enrolled_student(request,id):
    course = get_object_or_404(Course,id=id)
    students = course.students.all()
    
    context = {
        'course':course,
        'students':students,
        'check':2
    }
    
    return render(request,html_path_for_student_list,context)

@login_required(login_url='login_user')
def Course_wise_Student(request):
    courses = Course.objects.all()
    
    context = {
        'courses':courses
    }
    return render(request,"Course_app/Course_wise_Student.html",context)


@login_required(login_url='login_user')
def individual_student_detail(request,id):
    student = get_object_or_404(Student,id=id)
    context = {
        'student':student,
        'check':3
        }
    return render(request,html_path_for_student_list,context)




# Uder Authentication process
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request,f"Welcome {username}!")
                return redirect('course_list')
            else:
                messages.error(request,"Invalid usename or password!")
    else:
        form = AuthenticationForm()
    context = {
        'check' : 2,
        'form' : form,
    }
    return render(request,"Course_app/user_login_and_register_form.html",context)   

@login_required(login_url='login_user') 
def logout_user(request):
    logout(request)
    messages.info(request, "You have been Logout!")
    return redirect('login_user')



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created Successfully")
            return redirect('login_user')
    else:
        form = UserRegistrationForm()
    context = {
        'check' : 1,
        'form':form
    }
    
    return render(request,"Course_app/user_login_and_register_form.html",context)


def about(request):
    return render(request,"Course_app/about.html")

def services(request):
    return render(request,"Course_app/services.html")