from rest_framework import serializers
from ..models.perfume import Perfume

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = '__all__'