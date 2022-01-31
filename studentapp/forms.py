from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('assign_name','date','uploadby',)
        labels = {
            'assign_name':'Assignment Name',
            'date':'Date',
            'uploadby':'Uploadby'
        }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
    
# def save(self,commit=True):
#         user = super(NewUserForm,self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

  
       

         

    