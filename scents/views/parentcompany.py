from ..models.parentcompany import ParentCompany
from ..serializers.parentcompany import ParentCompanySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ParentCompanyViewSet(ModelViewSet):
    model = ParentCompany
    serializer_class = ParentCompanySerializer
    queryset = ParentCompany.objects.all()