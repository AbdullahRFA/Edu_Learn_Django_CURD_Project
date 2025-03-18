from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

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
        widget=forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your email'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Confirm your password'}),
        }
        
        
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        max_length=254, 
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    

class UserUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Old Password'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter New Password'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'})
    )