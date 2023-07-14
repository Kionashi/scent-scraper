from rest_framework import serializers
from ..models.accord import Accord

class AccordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accord
        fields = '__all__'