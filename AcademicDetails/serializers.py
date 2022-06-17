from AcademicDetails.models import AcademicDetails
from rest_framework import serializers
from Student.serializers import OnlyStudentDetailsSerializer

''' Taking Executive Login Details '''
class OnlyAcademicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDetails
        fields = '__all__'

class AcademicDetailsSerializer(serializers.ModelSerializer):
    student_userName = OnlyStudentDetailsSerializer()
    
    class Meta:
        model = AcademicDetails
        fields = '__all__'
