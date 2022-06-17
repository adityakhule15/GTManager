from AcademicDetails.models import HOD
from rest_framework import serializers
from College.serializers import CollegeDetailsSerializer


class OnlyHODDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HOD
        fields = '__all__'

class HODDetailsSerializer(serializers.ModelSerializer):
    college_userName = CollegeDetailsSerializer()
    class Meta:
        model = HOD
        fields = '__all__'