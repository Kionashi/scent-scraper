from ..models.designer import Designer
from ..serializers.designer import DesignerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DesignerViewSet(ModelViewSet):
    model = Designer
    serializer_class = DesignerSerializer
    queryset = Designer.objects.all()