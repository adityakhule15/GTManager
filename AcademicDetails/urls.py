from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.AcdemicDetailsList.postSave, name="postSave"),
        path('academicDetails/', views.AcdemicDetailsList.AcademicDetails, name="academicDetails"),
    ]