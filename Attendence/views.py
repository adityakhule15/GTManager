from AcademicDetails.models import Attendence
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from Attendence.serializers import AttendenceSerializer

 
@csrf_exempt
class AttendenceDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=Attendence()
        prod.teachers_userName_id=request.POST.get('teachers_userName')
        prod.date=request.POST.get('date')
        prod.present_id=request.POST.get('present')
        prod.save()

        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def AttendenceDetails(request):
        teachers_userName=request.POST.get('teachers_userName')
        date=request.POST.get('date')
        print(teachers_userName)
        Attendence1=Attendence.objects.filter(teachers_userName = teachers_userName, date = date).all()
        serializer = AttendenceSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'AttendenceDetails':total_Attendence}
        return JsonResponse(data)
  
    