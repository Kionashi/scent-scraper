from ..models.notegroup import NoteGroup
from ..serializers.notegroup import NoteGroupSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NoteGroupViewSet(ModelViewSet):
    model = NoteGroup
    serializer_class = NoteGroupSerializer
    queryset = NoteGroup.objects.all()