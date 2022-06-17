from AcademicDetails.models import AddmissionDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from AddmissionDetails.serializers import AddmissionDetailsSerializer 

 
@csrf_exempt
class AddmissionDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=AddmissionDetails()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.college_userName_id=request.POST.get('college_userName')
        prod.addmission_id=request.POST.get('addmission_id')
        prod.addmission_date=request.POST.get('addmission_date')
        prod.addmission_year=request.POST.get('addmission_year')
        prod.addmission_course=request.POST.get('addmission_course')
        prod.addmission_course_group=request.POST.get('addmission_course_group')
        prod.save()
    
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def AddmissionDetails(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        AddmissionDetails1=AddmissionDetails.objects.filter(student_userName = student_userName).all()
        serializer = AddmissionDetailsSerializer(AddmissionDetails1, many = True)
        total_AddmissionDetails1 = json.dumps(serializer.data)
        total_AddmissionDetails = json.loads(total_AddmissionDetails1)
        data = {'AddmissionDetails':total_AddmissionDetails}
        return JsonResponse(data)
  
    