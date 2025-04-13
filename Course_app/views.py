from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CourseForm, LessonForm, StudentForm, UserRegistrationForm, UserUpdateForm, UserPasswordChangeForm
from .models import Course, Lesson, Student

# 🔄 CBV Version (Class-Based View)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# for sending mail to get otp
import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import PasswordResetRequestForm
from django.contrib.auth.hashers import make_password





# html_path_variabl
html_path_delete_confirmation_form = "Course_app/delete_confirmation_form.html"
html_path_for_student_list="Course_app/student_list.html"
html_path_for_input_and_update="Course_app/input_and_update_form.html"

# Create your views here.
@login_required(login_url='login_user')
def course_list(request):
    courses = Course.objects.all()
    
    return render(request,"Course_app/course_list.html",{"courses":courses})

# CBV for course_list
# class CourseListView(LoginRequiredMixin, ListView):
#     model = Course
#     template_name = "Course_app/course_list.html"
#     context_object_name = "courses"
#     login_url = 'login_user'

@login_required(login_url='login_user')
def Course_Details(request, id):
    course = get_object_or_404(Course, id=id)
    lessons = course.lessons.all()

    # 🔁 Replace this with your actual logic to get the logged-in student
    student = Student.objects.first()  # Or use: request.user.student if connected to auth

    total_lessons = lessons.count()

    # Count how many lessons the student has completed for this course
    completed_lessons = student.completed_lesson.filter(course=course).count() if student else 0

    # Calculate progress percentage (avoid division by zero)
    percent_complete = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0

    context = {
        'course': course,
        'lessons': lessons,
        'student': student,
        'total_lessons': total_lessons,
        'completed_lessons': completed_lessons,
        'percent_complete': percent_complete,
    }

    return render(request, "Course_app/Course_details.html", context)

# CBV for course_details

# class CourseDetailView(LoginRequiredMixin, View):
#     login_url = 'login_user'  # Redirect to login if not authenticated

#     def get(self, request, id):
#         course = get_object_or_404(Course, id=id)
#         lessons = course.lessons.all()

#         # Get the logged-in student (assuming one-to-one relation with user)
#         try:
#             student = request.user.student
#         except Student.DoesNotExist:
#             student = None

#         total_lessons = lessons.count()
#         completed_lessons = (
#             student.completed_lesson.filter(course=course).count() if student else 0
#         )
#         percent_complete = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0

#         context = {
#             'course': course,
#             'lessons': lessons,
#             'student': student,
#             'total_lessons': total_lessons,
#             'completed_lessons': completed_lessons,
#             'percent_complete': percent_complete,
#         }

#         return render(request, "Course_app/Course_details.html", context)


@login_required
def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        # Optional: fallback by email
        try:
            student = Student.objects.get(email=request.user.email)
        except Student.DoesNotExist:
            return redirect('user_profile')  # Or show a message

    student.completed_lesson.add(lesson)
    return redirect('coursedetails', id=lesson.course.id)


#TODO has to be worked
@login_required
def uncomplete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Student profile not found.")
        return redirect('user_profile')

    if lesson in student.completed_lesson.all():
        student.completed_lesson.remove(lesson)
        messages.success(request, f"Marked '{lesson.title}' as incomplete.")
        
    print("User:", request.user)
    print("Is Authenticated:", request.user.is_authenticated)
    print("Student Exists:", Student.objects.filter(user=request.user).exists())
    print("Lesson ID:", lesson_id)
    
    return redirect('coursedetails', id=lesson.course.id)


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

# CBV for create_course

# class CourseCreateView(LoginRequiredMixin, CreateView):
#     model = Course
#     form_class = CourseForm
#     template_name = html_path_for_input_and_update 
#     login_url = 'login_user'
#     success_url = reverse_lazy('course_list')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Course added successfully!")
#         return response

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['check'] = 2  # Passing 'check' like in your FBV
#         return context




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


@login_required(login_url='login_user')
def user_profile(request):
    return render(request, 'Course_app/user_profile.html')


@login_required(login_url='login_user')
def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile')
    else:
        form = UserUpdateForm(instance=user)
    
    return render(request, 'Course_app/update_profile.html', {'form': form})

def about(request):
    return render(request,"Course_app/about.html")

def services(request):
    return render(request,"Course_app/services.html")


# Forget password and reset section

# Dictionary to store OTPs temporarily
otp_storage = {}

def send_otp(email):
    """Generate and send OTP to the user's email."""
    otp = random.randint(100000, 999999)  # Generate 6-digit OTP
    otp_storage[email] = otp  # Store OTP temporarily

    subject = "Password Reset OTP - EduLearn"
    message = f"Hello,\n\nYour OTP for password reset is: {otp}\n\nDo not share this OTP with anyone."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def request_password_reset(request):
    """Handle password reset request and send OTP."""
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            
            if user:
                send_otp(email)
                messages.success(request, "OTP has been sent to your email.")
                return redirect('verify_otp', email=email)  # Redirect to OTP verification
            else:
                messages.error(request, "No user found with this email.")
    
    else:
        form = PasswordResetRequestForm()
    
    return render(request, "Course_app/request_password_reset.html", {'form': form})

def verify_otp(request, email):
    """Verify the OTP entered by the user."""
    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        if otp_storage.get(email) and str(otp_storage[email]) == entered_otp:
            del otp_storage[email]  # Remove OTP after successful verification
            messages.success(request, "OTP verified successfully. Set a new password.")
            return redirect('reset_password', email=email)
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    
    return render(request, "Course_app/verify_otp.html", {'email': email})


def reset_password(request, email):
    """Allow the user to reset their password."""
    if request.method == "POST":
        new_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if new_password == confirm_password:
            user = User.objects.filter(email=email).first()
            if user:
                user.password = make_password(new_password)  # Hash the password
                user.save()
                messages.success(request, "Password reset successfully. Please login.")
                return render(request,'Course_app/password_reset_complete.html')
            else:
                messages.error(request, "User not found.")
        else:
            messages.error(request, "Passwords do not match. Try again.")
    
    return render(request, "Course_app/reset_password.html", {'email': email})



@login_required(login_url='login_user')
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(data=request.POST, user=request.user)  # ✅ Corrected form initialization
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # ✅ Keep user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect('password_change_complete')  # ✅ Redirect instead of re-rendering
    else:
        form = UserPasswordChangeForm(user=request.user)

    return render(request, 'Course_app/change_password.html', {'form': form})

def password_change_complete(request):
    return render(request, 'Course_app/password_change_complete.html')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseListAPI(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetailAPI(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Course

class EnrollStudentAPI(APIView):
    def post(self, request):
        student_email = request.data.get('email')
        student_name = request.data.get('name')
        roll = request.data.get('roll')
        course_id = request.data.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        student, created = Student.objects.get_or_create(
            email=student_email,
            defaults={'name': student_name, 'roll': roll}
        )

        student.enrolled_courses.add(course)
        return Response({'message': f'{student.email} has been enrolled in {course.title}'})