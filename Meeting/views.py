from AcademicDetails.models import Meeting
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import MeetingSerializer

 
@csrf_exempt
class MeetingList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=Meeting()
        prod.meeting_id=request.POST.get('meeting_id')
        prod.organiser_id_id=request.POST.get('teachers_userName')
        prod.time=request.POST.get('time')
        prod.date=request.POST.get('date')
        prod.message=request.POST.get('message')
        prod.status='Pending'
        prod.title=request.POST.get('title')
        prod.link='link'
        prod.type_of_meeting='type_of_meeting'
        prod.save()

        return HttpResponse("Success")        

    @csrf_exempt
    def PendingMeetings(request):
        organiser_id=request.POST.get('teachers_userName')
        print(organiser_id)
        Meeting1=Meeting.objects.filter(organiser_id = organiser_id, status='Pending').all()
        serializer = MeetingSerializer(Meeting1, many = True)
        total_Meeting1 = json.dumps(serializer.data)
        total_Meeting = json.loads(total_Meeting1)
        data = {'Meeting':total_Meeting}
        return JsonResponse(data)

    @csrf_exempt
    def CompletedMeetings(request):
        organiser_id=request.POST.get('teachers_userName')
        print(organiser_id)
        Meeting1=Meeting.objects.filter(organiser_id = organiser_id, status='Completed').all()
        serializer = MeetingSerializer(Meeting1, many = True)
        total_Meeting1 = json.dumps(serializer.data)
        total_Meeting = json.loads(total_Meeting1)
        data = {'Meeting':total_Meeting}
        return JsonResponse(data)

    @csrf_exempt
    def update(request):       

        Meeting.objects.filter(meeting_id=request.POST.get('meeting_id')).update(
        status='Completed',
        mom=request.POST.get('mom'),
        )
        
        return HttpResponse("Success")   
