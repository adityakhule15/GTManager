from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.AttendenceDetailsList.postSave, name="postSave"),
        path('attendenceDetails/', views.AttendenceDetailsList.AttendenceDetails, name="attendenceDetails"),
    ]