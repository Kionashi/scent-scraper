from ..models.accord import Accord
from ..serializers.accord import AccordSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AccordViewSet(ModelViewSet):
    model = Accord
    serializer_class = AccordSerializer
    queryset = Accord.objects.all()