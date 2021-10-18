from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('assign_name','date','uploadby',)
        labels = {
            'assign_name':'Assignment Name',
            'date':'Date',
            'uploadby':'Uploadby'
        }

    