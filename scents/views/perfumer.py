from ..models.perfumer import Perfumer
from ..serializers.perfumer import PerfumerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PerfumerViewSet(ModelViewSet):
    model = Perfumer
    serializer_class = PerfumerSerializer
    queryset = Perfumer.objects.all()