from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.MeetingList.postSave, name="postSave"),
        path('pendingMeetings/', views.MeetingList.PendingMeetings, name="pendingMeetings"),
        path('completedMeetings/', views.MeetingList.CompletedMeetings, name="completedMeetings"),
        path('update/', views.MeetingList.update, name="update"),
    ]