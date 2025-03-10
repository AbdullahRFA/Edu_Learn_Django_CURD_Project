from django import forms

from .models import Course,Lesson,Student

class courseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','descriptions','durations','thumbnail']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'descriptions':forms.Textarea(attrs={'class':'form-control'}),
            'durations':forms.NumberInput(attrs={'class':'form-control'}),
        }
        
class lessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course','title','content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }