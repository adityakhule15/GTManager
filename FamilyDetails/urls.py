from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.FamilyDetailsList.postSave, name="postSave"),
        path('familyDetails/', views.FamilyDetailsList.FamilyDetails, name="familyDetails"),
    ]