from ..models.industry import Industry
from ..serializers.industry import IndustrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class IndustryViewSet(ModelViewSet):
    model = Industry
    serializer_class = IndustrySerializer
    queryset = Industry.objects.all()