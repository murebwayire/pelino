from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.forms import Contactform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from conference.models import Conference


def home(request):
    return render(request, 'core/home.html')


def contact(request):
    if request.method=='POST':
        form=Contactform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            pass
            
        messages.success(request, '...')
        return redirect('home')

    else:

        form=Contactform()     
        return render(request, 'core/contact.html',{'form':form})





def about(request):
     return render(request, 'core/about.html')


def register_user(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username , password=password)
            login(request, user)

        return redirect('home')
            
    else:

        form = UserCreationForm()        
    return render(request, 'registration/register_user.html', {'form': form})   