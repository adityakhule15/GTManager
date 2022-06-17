from AcademicDetails.models import FamilyDetails
from rest_framework import serializers
from Student.serializers import OnlyStudentDetailsSerializer

''' Taking Executive Login Details '''
class OnlyFamilyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetails
        fields = '__all__'

class FamilyDetailsSerializer(serializers.ModelSerializer):
    student_userName = OnlyStudentDetailsSerializer()
    
    class Meta:
        model = FamilyDetails
        fields = '__all__'
