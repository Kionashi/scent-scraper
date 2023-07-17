from django.db import models
from .base import BaseModel

class PerfumeNote(BaseModel):
    class Positions(models.TextChoices):
        TOP = 'top'
        MID = 'mid'
        BOT = 'bot'
        PLAIN = 'plain'

    perfume = models.ForeignKey('Perfume', on_delete=models.CASCADE)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)
    position = models.CharField(max_length=5, choices=Positions.choices, default=Positions.PLAIN)
    class Meta:
        db_table = 'scents_perfume_note'