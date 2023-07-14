from rest_framework import serializers
from ..models.perfumeaccord import PerfumeAccord

class PerfumeAccordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfumeAccord
        fields = '__all__'