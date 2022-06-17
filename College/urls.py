from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.CollegeDetailsList.postSave, name="postSave"),
        path('collegeDetails/', views.CollegeDetailsList.CollegeDetails, name="collegeDetails"),
        path('update/', views.CollegeDetailsList.update, name="update"),
        path('updateImage/', views.CollegeDetailsList.updateImage, name="updateImage"),
    ]