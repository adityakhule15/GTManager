from AcademicDetails.models import AddmissionDetails
from rest_framework import serializers
from College.serializers import CollegeDetailsSerializer
from Student.serializers import OnlyStudentDetailsSerializer

''' Taking Executive Login Details '''
class OnlyAddmissionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddmissionDetails
        fields = '__all__'

class AddmissionDetailsSerializer(serializers.ModelSerializer):
    college_userName = CollegeDetailsSerializer()
    student_userName = OnlyStudentDetailsSerializer()
    
    class Meta:
        model = AddmissionDetails
        fields = '__all__'
