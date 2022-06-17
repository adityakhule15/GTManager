from AcademicDetails.models import AppointmentDetails
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = AppointmentDetails
        fields = '__all__'


