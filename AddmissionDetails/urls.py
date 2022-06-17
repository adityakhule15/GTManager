from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.AddmissionDetailsList.postSave, name="postSave"),
        path('addmissionDetails/', views.AddmissionDetailsList.AddmissionDetails, name="addmissionDetails"),
    ]