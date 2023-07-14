from rest_framework import serializers
from ..models.notegroup import NoteGroup

class NoteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteGroup
        fields = '__all__'