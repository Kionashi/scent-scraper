from rest_framework import serializers
from ..models.parentcompany import ParentCompany

class ParentCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCompany
        fields = '__all__'