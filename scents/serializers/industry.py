from rest_framework import serializers
from ..models.industry import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'