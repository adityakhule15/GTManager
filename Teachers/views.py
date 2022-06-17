from .serializers import *
from AcademicDetails.models import HOD, Login, TeachersDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class TeacherDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('teacher_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position_teacher = 'True'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=TeachersDetails()
        prod.college_userName_id=request.POST.get('college_userName')
        prod.hod_userName_id=request.POST.get('hod_userName')
        prod.teachers_userName_id=usname
        prod.teachers_name=request.POST.get('teachers_name')
        prod.teachers_email=request.POST.get('teachers_email')
        prod.teachers_mobileNumber=request.POST.get('teachers_mobileNumber')
        prod.teachers_groupName=request.POST.get('teachers_groupName')
        prod.teachers_image='/teachers_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def TeacherDetails(request):
        teacher_userName = request.POST.get('teacher_userName')
        print(teacher_userName)
        TeacherDetails1=TeachersDetails.objects.filter(teachers_userName = teacher_userName).all()
        serializer = TeacherDetailsSerializer(TeacherDetails1, many = True)
        total_TeacherDetails1 = json.dumps(serializer.data)
        total_TeacherDetails = json.loads(total_TeacherDetails1)
        data = {'TeacherDetails':total_TeacherDetails}
        return JsonResponse(data)

    @csrf_exempt
    def TeacherList(request):
        hod_userName = request.POST.get('hod_userName')
        print(hod_userName)
        TeacherDetails1=TeachersDetails.objects.filter(hod_userName = hod_userName).all()
        serializer = TeacherDetailsSerializer(TeacherDetails1, many = True)
        total_TeacherDetails1 = json.dumps(serializer.data)
        total_TeacherDetails = json.loads(total_TeacherDetails1)
        data = {'TeacherList':total_TeacherDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        TeachersDetails.objects.filter(teacher_userName = request.POST.get('teacher_userName')).update(
        teachers_name=request.POST.get('teachers_name'),
        teachers_email=request.POST.get('teachers_email'),
        teachers_mobileNumber=request.POST.get('teachers_mobileNumber'),
        teachers_groupName=request.POST.get('teachers_groupName'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('teacher_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/teachers_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
