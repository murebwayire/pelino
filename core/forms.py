from django import forms
from django.forms import ModelForm
from core.models import Contact
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm



class Contactform(forms.ModelForm):
    class Meta:
        model= Contact
        fields=('name','email','subject','message')
        
        labels = {

            'name':'Name:',
            'email':'Email',
            'subject':'Subject',
            'message':'Message',
          
        }

        widgets ={
            
           'name':forms.TextInput(attrs={ 'class':'form-control mb-4'}),
    
            'email':forms.EmailInput(attrs={ 'class':'form-control mb-4 '}),
           'subject':forms.TextInput(attrs={ 'class':'form-control mb-4'}),

            'message':forms.Textarea(attrs={ 'class':'form-control mb-4'}),
             
        }


# class RegisterUserForm(UserCreationForm):
