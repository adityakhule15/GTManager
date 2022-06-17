from datetime import date
from AcademicDetails.models import AppointmentDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import AppointmentSerializer 

 
@csrf_exempt
class AppointmentList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=AppointmentDetails()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.teachers_userName_id=request.POST.get('teachers_userName')
        prod.reason_of_appintment=request.POST.get('reason_of_appintment')
        prod.date_of_appoinment=request.POST.get('date_of_appoinment')
        prod.time_of_appoinment=request.POST.get('time_of_appoinment')
        prod.approval_status='Pending'
        prod.save()
    
        return HttpResponse("Success")
        

    @csrf_exempt
    def StudentAppointmentPending(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        Appointment1=AppointmentDetails.objects.filter(student_userName = student_userName, approval_status='Pending').all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)
  
    @csrf_exempt
    def StudentAppointmentApprovrd(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        Appointment1=AppointmentDetails.objects.filter(student_userName = student_userName, approval_status='Approved').all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)
    
    @csrf_exempt
    def update(request):       

        AppointmentDetails.objects.filter(id=request.POST.get('id')).update(
        approval_status=request.POST.get('status'),
        )
        
        return HttpResponse("Success")   

    @csrf_exempt
    def TeacherAppointmentPending(request):
        teachers_userName=request.POST.get('teachers_userName')
        print(teachers_userName)
        Appointment1=AppointmentDetails.objects.filter(teachers_userName = teachers_userName, approval_status='Pending').all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)
    
    @csrf_exempt
    def TeacherAppointmentApprovrd(request):
        teachers_userName=request.POST.get('teachers_userName')
        print(teachers_userName)
        Appointment1=AppointmentDetails.objects.filter(teachers_userName = teachers_userName, approval_status='Approved').all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)

    @csrf_exempt
    def TeachersTodaysAppointment(request):
        teachers_userName=request.POST.get('teachers_userName')
        print(teachers_userName)
        Appointment1=AppointmentDetails.objects.filter(teachers_userName = teachers_userName, approval_status='Approved',date_of_appoinment = date.today).all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)

    @csrf_exempt
    def StudentsTodaysAppointment(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        Appointment1=AppointmentDetails.objects.filter(student_userName = student_userName, approval_status='Approved',date_of_appoinment = date.today).all()
        serializer = AppointmentSerializer(Appointment1, many = True)
        total_Appointment1 = json.dumps(serializer.data)
        total_Appointment = json.loads(total_Appointment1)
        data = {'Appointment':total_Appointment}
        return JsonResponse(data)