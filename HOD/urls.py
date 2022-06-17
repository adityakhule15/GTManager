from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.HODDetailsList.postSave, name="postSave"),
        path('hodDetails/', views.HODDetailsList.HODDetails, name="hodDetails"),
        path('hodList/', views.HODDetailsList.HODList, name="hodList"),
        path('update/', views.HODDetailsList.update, name="update"),
        path('updateImage/', views.HODDetailsList.updateImage, name="updateImage"),
    ]