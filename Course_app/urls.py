from django.contrib import admin
from django.urls import path
from Course_app import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('details/<int:id>/',views.Course_Details,name='coursedetails'),
    
    
    path('create_course/',views.create_course,name='create_course'),
    path('course_edit/<int:id>/',views.course_edit,name='course_edit'),
    path('course_delete/<int:id>/',views.course_delete,name='course_delete'),
    
    
    path('create_lesson/',views.create_lesson,name='create_lesson'),
    path('lesson_edit/<int:id>/',views.lesson_edit,name='lesson_edit'),
    path('lesson_delete/<int:id>/',views.lesson_delete,name='lesson_delete'),
    
    
    
    path('student_list/',views.student_list,name='student_list'),
    path('Enroll_student/',views.Enroll_student,name='Enroll_student'),
    path('update_student/<int:id>',views.update_student,name='update_student'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    
    
    
    path('individual_course_enrolled_student/<int:id>',views.individual_course_enrolled_student,name='individual_course_enrolled_student'),
    
    
    
]
