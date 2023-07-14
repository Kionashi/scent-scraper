from ..models.perfume import Perfume
from ..serializers.perfume import PerfumeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PerfumeViewSet(ModelViewSet):
    model = Perfume
    serializer_class = PerfumeSerializer
    queryset = Perfume.objects.all()