from .serializers import HODDetailsSerializer
from AcademicDetails.models import HOD, Login
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class HODDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('hod_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position_hod = 'True'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=HOD()
        prod.college_userName_id=request.POST.get('college_userName')
        prod.hod_userName_id=usname
        prod.hod_name=request.POST.get('hod_name')
        prod.hod_departmentName=request.POST.get('hod_departmentName')
        prod.hod_mobileNumber=request.POST.get('hod_mobileNumber')
        prod.hod_email=request.POST.get('hod_email')
        prod.hod_image='/hod_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def HODDetails(request):
        hod_userName = request.POST.get('hod_userName')
        print(hod_userName)
        HODDetails1=HOD.objects.filter(hod_userName = hod_userName).all()
        serializer = HODDetailsSerializer(HODDetails1, many = True)
        total_HODDetails1 = json.dumps(serializer.data)
        total_HODDetails = json.loads(total_HODDetails1)
        data = {'HODDetails':total_HODDetails}
        return JsonResponse(data)

    @csrf_exempt
    def HODList(request):
        college_userName = request.POST.get('college_userName')
        print(college_userName)
        HODDetails1=HOD.objects.filter(college_userName = college_userName).all()
        serializer = HODDetailsSerializer(HODDetails1, many = True)
        total_HODDetails1 = json.dumps(serializer.data)
        total_HODDetails = json.loads(total_HODDetails1)
        data = {'HODList':total_HODDetails}
        return JsonResponse(data)

    @csrf_exempt
    def update(request):       

        HOD.objects.filter(hod_userName = request.POST.get('hod_userName')).update(
        hod_name=request.POST.get('hod_name'),
        hod_departmentName=request.POST.get('hod_departmentName'),
        hod_email=request.POST.get('hod_email'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('hod_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/hod_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
