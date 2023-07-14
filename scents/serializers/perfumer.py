from rest_framework import serializers
from ..models.perfumer import Perfumer

class PerfumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfumer
        fields = '__all__'