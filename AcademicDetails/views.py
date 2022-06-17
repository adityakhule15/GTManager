from .serializers import AcademicDetailsSerializer
from AcademicDetails.models import AcademicDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt 

 
@csrf_exempt
class AcdemicDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=AcademicDetails()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.exam_name=request.POST.get('exam_name')
        prod.institute=request.POST.get('institute')
        prod.exam_taken_by=request.POST.get('exam_taken_by')
        prod.percentage=request.POST.get('percentage')
        prod.total_marks=request.POST.get('total_marks')
        prod.obtain_marks=request.POST.get('obtain_marks')
        prod.year_passing=request.POST.get('year_passing')
        prod.result=request.POST.get('result')
        prod.subject_back=request.POST.get('subject_back')
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  Academic Details from database 
    @csrf_exempt
    def AcademicDetails(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        CollegeDetails1=AcademicDetails.objects.filter(student_userName = student_userName).all()
        serializer = AcademicDetailsSerializer(CollegeDetails1, many = True)
        total_AcademicDetails1 = json.dumps(serializer.data)
        total_AcademicDetails = json.loads(total_AcademicDetails1)
        data = {'AcademicDetails':total_AcademicDetails}
        return JsonResponse(data)
  
    