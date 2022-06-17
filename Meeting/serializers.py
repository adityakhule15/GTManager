from AcademicDetails.models import Meeting
from rest_framework import serializers
from Teachers.serializers import OnlyTeacherDetailsSerializer


class MeetingSerializer(serializers.ModelSerializer):
    organiser_id = OnlyTeacherDetailsSerializer()
    
    class Meta:
        model = Meeting
        fields = '__all__'
