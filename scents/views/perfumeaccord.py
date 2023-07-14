from ..models.perfumeaccord import PerfumeAccord
from ..serializers.perfumeaccord import PerfumeAccordSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PerfumeAccordViewSet(ModelViewSet):
    model = PerfumeAccord
    serializer_class = PerfumeAccordSerializer
    queryset = PerfumeAccord.objects.all()