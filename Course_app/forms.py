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