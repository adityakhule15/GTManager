"""GTManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AcademicDetails/', include('AcademicDetails.urls')),
    path('AddmissionDetails/', include('AddmissionDetails.urls')),
    path('Appointment/', include('Appointment.urls')),
    path('Attendence/', include('Attendence.urls')),
    path('Complaint/', include('Complaint.urls')),
    path('College/', include('College.urls')),
    path('FamilyDetails/', include('FamilyDetails.urls')),
    path('ForgotPasswordAndCreatPassword/', include('ForgotPasswordAndCreatPassword.urls')),
    path('HOD/', include('HOD.urls')),
    path('Login/', include('Login.urls')),
    path('Meeting/', include('Meeting.urls')),
    path('PreviousGT/', include('PreviousGT.urls')),
    path('Student/', include('Student.urls')),
    path('Teachers/', include('Teachers.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)