from django.contrib import admin
from django.urls import path
from Course_app import views

# For CBV
from .views import CourseListView, CourseDetailView

urlpatterns = [
    # path('',views.course_list,name='course_list'),
    path('', CourseListView.as_view(), name='course_list'),

    # path('details/<int:id>/',views.Course_Details,name='coursedetails'),
    path('details/<int:id>/', CourseDetailView.as_view(), name='coursedetails'),
    
    
    path('create_course/',views.create_course,name='create_course'),
    path('course_edit/<int:id>/',views.course_edit,name='course_edit'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),
    
    
    path('create_lesson/',views.create_lesson,name='create_lesson'),
    path('lesson_edit/<int:id>/',views.lesson_edit,name='lesson_edit'),
    path('lesson_delete/<int:id>/',views.lesson_delete,name='lesson_delete'),
    
    
    
    path('student_list/',views.student_list,name='student_list'),
    path('Enroll_student/',views.Enroll_student,name='Enroll_student'),
    path('update_student/<int:id>/',views.update_student,name='update_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    
    
    
    path('individual_course_enrolled_student/<int:id>/',views.individual_course_enrolled_student,name='individual_course_enrolled_student'),
    path('Course_wise_Student/',views.Course_wise_Student,name='Course_wise_Student'),
    path('individual_student_detail/<int:id>/',views.individual_student_detail,name='individual_student_detail'),
    
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('register_user/',views.register_user,name='register_user'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    
    
    
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    
    
    
    path('forgot_password/', views.request_password_reset, name='forgot_password'),
    path('verify_otp/<str:email>/', views.verify_otp, name='verify_otp'),
    path('reset_password/<str:email>/', views.reset_password, name='reset_password'),
    path('change_password', views.change_password, name='change_password'),
    path('change_password', views.change_password, name='change_password'),
    path('password_change_complete', views.password_change_complete, name='password_change_complete'),
    
    
    
    path('lesson/<int:lesson_id>/complete/', views.complete_lesson, name='complete_lesson'),
    # path('lesson/<int:lesson_id>/uncomplete/', views.uncomplete_lesson, name='uncomplete_lesson'),
    
    
]
