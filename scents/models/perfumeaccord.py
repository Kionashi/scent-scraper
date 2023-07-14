from django.db import models
from .base import BaseModel

class PerfumeAccord(BaseModel):
    perfume = models.ForeignKey('Perfume', on_delete=models.CASCADE)
    accord = models.ForeignKey('Accord', on_delete=models.CASCADE)
    concentration = models.DecimalField(max_digits=5, decimal_places=2)