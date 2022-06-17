from AcademicDetails.models import PreviousGTDetails
from rest_framework import serializers
from Student.serializers import OnlyStudentDetailsSerializer


class OnlyPreviousGTDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousGTDetails
        fields = '__all__'

class PreviousGTDetailsSerializer(serializers.ModelSerializer):
    student_userName = OnlyStudentDetailsSerializer()
    class Meta:
        model = PreviousGTDetails
        fields = '__all__'