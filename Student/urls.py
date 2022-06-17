from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.StudentDetailsList.postSave, name="postSave"),
        path('personalityPrediction/', views.StudentDetailsList.personalityPrediction, name="personalityPrediction"),
        path('studentDetails/', views.StudentDetailsList.StudentDetails, name="studentDetails"),
        path('studentList/', views.StudentDetailsList.StudentList, name="studentList"),
        path('updatePersonalityCheck/', views.StudentDetailsList.updatePersonalityCheck, name="updatePersonalityCheck"),
        path('update/', views.StudentDetailsList.update, name="update"),
        path('updateImage/', views.StudentDetailsList.updateImage, name="updateImage"),
    ]