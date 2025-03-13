from django import forms
from .models import Course, Lesson, Student

class courseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'descriptions', 'durations', 'thumbnail']  # ✅ Fixed "durations" to "duration"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control'}),
            'durations': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class lessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),  # ✅ Fixed to use Select
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','email','enrolled_courses']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'enrolled_courses':forms.CheckboxSelectMultiple(attrs={'class':'form-control'})
        }