from AcademicDetails.models import PreviousGTDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import PreviousGTDetailsSerializer

 
@csrf_exempt
class PreviousGTDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=PreviousGTDetails()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.year=request.POST.get('year')
        prod.gt_name=request.POST.get('gt_name')
        prod.save()

        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def PreviousGTDetails(request):
        student_userName=request.POST.get('student_userName')
        print(student_userName)
        PreviousGTDetails1=PreviousGTDetails.objects.filter(student_userName = student_userName).all()
        serializer = PreviousGTDetailsSerializer(PreviousGTDetails1, many = True)
        total_PreviousGTDetails1 = json.dumps(serializer.data)
        total_PreviousGTDetails = json.loads(total_PreviousGTDetails1)
        data = {'PreviousGTDetails':total_PreviousGTDetails}
        return JsonResponse(data)
  
    