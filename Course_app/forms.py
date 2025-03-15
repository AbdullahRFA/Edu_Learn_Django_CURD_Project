from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lesson, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'descriptions', 'durations', 'thumbnail']  # ✅ Fixed "durations" to "duration"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'durations': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),  # ✅ Bootstrap uses `form-select`
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter lesson content...'}),
        }
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email', 'enrolled_courses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enrolled_courses': forms.CheckboxSelectMultiple()  # ✅ Removed class="form-control" (not needed)
        }
        


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }