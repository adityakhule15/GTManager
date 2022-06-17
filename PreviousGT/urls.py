from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.PreviousGTDetailsList.postSave, name="postSave"),
        path('previousGTDetails/', views.PreviousGTDetailsList.PreviousGTDetails, name="previousGTDetails"),
    ]