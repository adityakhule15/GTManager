from AcademicDetails.models import College
from rest_framework import serializers

''' Taking Executive Login Details '''
class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

