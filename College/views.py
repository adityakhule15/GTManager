from .serializers import CollegeDetailsSerializer
from AcademicDetails.models import Login, College
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class CollegeDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('college_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position_college = 'True'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=College()
        prod.college_userName_id=usname
        prod.college_name=request.POST.get('college_name')
        prod.college_principal_name=request.POST.get('college_principal_name')
        prod.college_email=request.POST.get('college_email')
        # image=request.POST['image'],
        # print(image[0])
        # imgdata = base64.b64decode(image[0])
        # print(usname)
        # path = settings.MEDIA_ROOT + '/college_images/' + usname + '.jpeg'
        # print(path)
        # with open(path, 'wb') as f:
        #     f.write(imgdata)
        prod.college_image='/college_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def CollegeDetails(request):
        college_userName = request.POST.get('college_userName')
        print(college_userName)
        CollegeDetails1=College.objects.filter(college_userName = college_userName).all()
        serializer = CollegeDetailsSerializer(CollegeDetails1, many = True)
        total_CollegeDetails1 = json.dumps(serializer.data)
        total_CollegeDetails = json.loads(total_CollegeDetails1)
        data = {'CollegeDetails':total_CollegeDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        College.objects.filter(college_userName = request.POST.get('college_userName')).update(
        college_name=request.POST.get('college_name'),
        college_principal_name=request.POST.get('college_principal_name'),
        college_email=request.POST.get('college_email'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('college_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/college_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
