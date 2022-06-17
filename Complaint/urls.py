from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.ComplaintList.postSave, name="postSave"),
        path('complaintDetails/', views.ComplaintList.ComplaintDetails, name="complaintDetails"),
        path('complaintPost/', views.ComplaintList.ComplaintPost, name="complaintPost"),
    ]