from AcademicDetails.models import Complaint
from rest_framework import serializers

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
