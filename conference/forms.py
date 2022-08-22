from django import forms

from conference.models import Conference, Speaker,Participant,Schedule


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
  

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = '__all__'
        
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'        
        
       


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'start_date', 'end_date', 'venue', 'entry_fee', 'speakers']
