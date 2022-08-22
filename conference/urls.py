from django.urls import path
from conference import views

urlpatterns = [
    path('all', views.conferences, name='conferences'),
    # localhost:8000/conference/python
    # localhost:8000/conference/software-development
    path('<int:id>', views.conference_detail, name="conference-detail"),
    path('<int:id>/edit', views.conference_edit, name="conference-update"),
    # localhost:8000/conference/software-development/register
    # path('<slug:name>/register', views.conference_registration),
    # path('<int:year>', views.yearly_conferences)
    path('add', views.add_conf, name='add-conference'),
    path('delete_conf/<int:id>', views.delete_conf, name='delete_conf'),
    # path('speakers/', views.speakers, name='speakers'),
    path('conf/', views.conf, name='conf'),
    path('view_conf/<int:id>', views.view_conf, name='view_conf'),
    path('add_speakers/', views.add_speakers, name='add_speakers'), 
    path('delete_speaker/<int:id>', views. delete_speaker, name="delete_speaker"),
    path('speaker_edit/<int:id>', views.speaker_edit, name="speaker_edit"),
    path('delete_participant/<int:id>', views.delete_participant, name='delete_participant'),
    path('search_conf/', views.search_conf, name="search_conf"),
    path('<int:id>/participant_edit', views.participant_edit, name="participant_edit"), 
   

   

]

