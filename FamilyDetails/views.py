from AcademicDetails.models import FamilyDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from FamilyDetails.serializers import FamilyDetailsSerializer

 
@csrf_exempt
class FamilyDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=FamilyDetails()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.fatherName=request.POST.get('fatherName')
        prod.brotherName=request.POST.get('brotherName')
        prod.sisterName=request.POST.get('sisterName')
        prod.spouseName=request.POST.get('spouseName')
        prod.fatherOccupation=request.POST.get('fatherOccupation')
        prod.motherOccupation=request.POST.get('motherOccupation')
        prod.spouseOccupation=request.POST.get('spouseOccupation')
        prod.fatherIncome=request.POST.get('fatherIncome')
        prod.motherIncome=request.POST.get('motherIncome')
        prod.spouseIncome=request.POST.get('spouseIncome')
        prod.save()
    
        return HttpResponse("Success")
            

    class Meta:
        db_table = "familyDetails"
    # Getting  College Details from database 
    @csrf_exempt
    def FamilyDetails(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        FamilyDetails1=FamilyDetails.objects.filter(student_userName = student_userName).all()
        serializer = FamilyDetailsSerializer(FamilyDetails1, many = True)
        total_FamilyDetails1 = json.dumps(serializer.data)
        total_FamilyDetails = json.loads(total_FamilyDetails1)
        data = {'FamilyDetails':total_FamilyDetails}
        return JsonResponse(data)
  
    