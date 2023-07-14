from rest_framework import serializers
from ..models.designer import Designer

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'