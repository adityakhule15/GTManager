from AcademicDetails.models import StudentDetails
from rest_framework import serializers
from Teachers.serializers import OnlyTeacherDetailsSerializer
from College.serializers import CollegeDetailsSerializer
from HOD.serializers import HODDetailsSerializer


class OnlyStudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'

class StudentDetailsSerializer(serializers.ModelSerializer):
    college_userName = CollegeDetailsSerializer()
    hod_userName = HODDetailsSerializer()
    teachers_userName = OnlyTeacherDetailsSerializer()
    class Meta:
        model = StudentDetails
        fields = '__all__'