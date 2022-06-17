from AcademicDetails.models import Attendence
from rest_framework import serializers
from Student.serializers import OnlyStudentDetailsSerializer
from Teachers.serializers import OnlyTeacherDetailsSerializer

''' Taking Executive Login Details '''
class OnlyAttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    teachers_userName = OnlyTeacherDetailsSerializer()
    present = OnlyStudentDetailsSerializer()
    
    class Meta:
        model = Attendence
        fields = '__all__'
