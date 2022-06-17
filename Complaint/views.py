from AcademicDetails.models import Complaint
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import ComplaintSerializer

 
@csrf_exempt
class ComplaintList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=Complaint()
        prod.teachers_userName_id=request.POST.get('teachers_userName')
        prod.student_username_id=request.POST.get('student_userName')
        prod.student_name=request.POST.get('student_name')
        prod.title=request.POST.get('title')
        prod.description=request.POST.get('description')
        prod.save()

        return HttpResponse("Success")
        

    @csrf_exempt
    def ComplaintPost(request):
        student_username=request.POST.get('student_userName')
        print(student_username)
        Complaint1=Complaint.objects.filter(student_username = student_username).all()
        serializer = ComplaintSerializer(Complaint1, many = True)
        total_Complaint1 = json.dumps(serializer.data)
        total_Complaint = json.loads(total_Complaint1)
        data = {'Complaint':total_Complaint}
        return JsonResponse(data)


    @csrf_exempt
    def ComplaintDetails(request):
        teachers_userName=request.POST.get('teachers_userName')
        print(teachers_userName)
        Complaint1=Complaint.objects.filter(teachers_userName = teachers_userName).all()
        serializer = ComplaintSerializer(Complaint1, many = True)
        total_Complaint1 = json.dumps(serializer.data)
        total_Complaint = json.loads(total_Complaint1)
        data = {'Complaints':total_Complaint}
        return JsonResponse(data)
    