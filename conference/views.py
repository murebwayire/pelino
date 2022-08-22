from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect

from conference.forms import ParticipantForm, SpeakerForm, ConferenceForm,ScheduleForm
from conference.models import Conference, Speaker, Participant,Schedule
from django.contrib import messages
from django.http import HttpResponseRedirect


def conferences(request):
    confs = Conference.objects.order_by('-created')
    return render(request,
                  'conference/conferences.html',
                  {'conferences': confs})


def conference_detail(request, id):
    all_conference=Conference.objects.all()
    speaker = Speaker.objects.all()
    schedule= Schedule.objects.filter(conference=id)
    conf = get_object_or_404(Conference, id=id)
    if request.method == "POST":
        form = ParticipantForm(request.POST, initial={'conference':conf})
        if form.is_valid():
            form.save()
        else:
            pass

    else:
        form =ParticipantForm(initial={'conference':conf})  

    return render(request,
                  'conference/conference_detail.html',
                  {'all': all_conference,'conference': conf,'speaker':speaker, 'schedule':schedule , 'form':form, })



def yearly_conferences(request, year):
    return HttpResponse(year + "Conferences")


@login_required
def add_conf(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('conferences')
    else:
        form = ConferenceForm()
    return render(request, 'conference/add_conference.html', {'form': form})


@login_required()
def conference_edit(request, id):
    conf = get_object_or_404(Conference, id=id)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conf)
        if form.is_valid():
            form.save()
        return redirect('conf')
    
    else:
        form = ConferenceForm(instance=conf)
    return render(request, 'conference/edit_conference.html', {'form': form})



def delete_conf(request,id):
    conf=Conference.objects.get(id=id)
    conf.delete()
    messages.success(request,"..")
    return redirect('conf')
   


def conf(request):
    all_member=Speaker.objects.all()
    conf= Conference.objects.all()
    part= Participant.objects.all()
    if request.method=="POST":
        form = ScheduleForm(request.POST or None)
        if form.is_valid():
            form.save()
           
        else:
            pass
        return redirect('conferences')
    else:
        form =ScheduleForm()        
    
    return render(request,'core/manage.html',{'conf':conf,'all':all_member,'part':part , 'form':form})

 


def add_speakers(request):
    if request.method =="POST":
        form =SpeakerForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('home')
    else:
           
        form=SpeakerForm()    
    return render(request,'conference/add_speaker.html',{'form':form})          


def delete_speaker(request,id):
    speaker=Speaker.objects.get(id=id)
    speaker.delete()
    return redirect('conf')

    
def speaker_edit(request,id):

    speaker=Speaker.objects.get(id=id)
    form =SpeakerForm( request.POST or None, request.FILES or None , instance=speaker  )
    if form.is_valid():
        form.save()
        return redirect('conf')

    return render(request, 'conference/edit_speaker.html', {'speaker': speaker, 'form': form})


def delete_participant(request,id):
    parti=Participant.objects.get(id=id)
    parti.delete()
    return redirect('conf')   


def search_conf(request):
    if request.method=="POST":
        searched = request.POST[ "searched" ]
        #    searched = request.POST["searched"]
        st= Conference.objects.filter(title__contains=searched)
   
    return render(request, 'conference/search_conf.html',{'a':searched , 'st':st})   
    



def participant_edit(request,id):
    parti=Participant.objects.get(id=id)
    form =ParticipantForm( request.POST or None , instance=parti)
    if form.is_valid():
        form.save()
        return redirect('conf')
    return render(request, 'conference/participant_edit.html', {'form': form})

def view_conf(request,id):
    all= Conference.objects.get(id=id)
    return render(request, 'conference/view_conf.html', {'all': all})


          
  

