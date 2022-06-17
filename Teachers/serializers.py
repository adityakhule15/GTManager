from AcademicDetails.models import TeachersDetails
from rest_framework import serializers
from College.serializers import CollegeDetailsSerializer
from HOD.serializers import HODDetailsSerializer


class OnlyTeacherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersDetails
        fields = '__all__'

class TeacherDetailsSerializer(serializers.ModelSerializer):
    college_userName = CollegeDetailsSerializer()
    hod_userName = HODDetailsSerializer()
    class Meta:
        model = TeachersDetails
        fields = '__all__'