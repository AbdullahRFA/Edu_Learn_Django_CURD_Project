from django.contrib import admin
from django.urls import path
from Course_app import views

urlpatterns = [
    path('',views.course_list,name='course_list'),
    path('details/<int:id>/',views.Course_Details,name='coursedetails'),
]
