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
]
