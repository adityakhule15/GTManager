from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.TeacherDetailsList.postSave, name="postSave"),
        path('teacherList/', views.TeacherDetailsList.TeacherList, name="teacherList"),
        path('teacherDetails/', views.TeacherDetailsList.TeacherDetails, name="teacherDetails"),
        path('update/', views.TeacherDetailsList.update, name="update"),
        path('updateImage/', views.TeacherDetailsList.updateImage, name="updateImage"),
    ]