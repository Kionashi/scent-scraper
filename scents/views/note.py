from ..models.note import Note
from ..serializers.note import NoteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NoteViewSet(ModelViewSet):
    model = Note
    serializer_class = NoteSerializer
    queryset = Note.objects.all()