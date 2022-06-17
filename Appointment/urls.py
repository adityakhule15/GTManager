from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.AppointmentList.postSave, name="postSave"),
        path('studentAppointmentPending/', views.AppointmentList.StudentAppointmentPending, name="studentAppointmentPending"),
        path('studentAppointmentApprovrd/', views.AppointmentList.StudentAppointmentApprovrd, name="studentAppointmentApprovrd"),
        path('update/', views.AppointmentList.update, name="update"),
        path('teacherAppointmentPending/', views.AppointmentList.TeacherAppointmentPending, name="teacherAppointmentPending"),
        path('teacherAppointmentApprovrd/', views.AppointmentList.TeacherAppointmentApprovrd, name="teacherAppointmentApprovrd"),
        path('teachersTodaysAppointment/', views.AppointmentList.TeachersTodaysAppointment, name="teachersTodaysAppointment"),
        path('studentsTodaysAppointment/', views.AppointmentList.StudentsTodaysAppointment, name="studentsTodaysAppointment"),
    ]