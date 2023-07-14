from ..models.country import Country
from ..serializers.country import CountrySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CountryViewSet(ModelViewSet):
    model = Country
    serializer_class = CountrySerializer
    queryset = Country.objects.all()