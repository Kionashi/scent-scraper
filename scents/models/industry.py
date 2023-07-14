from django.db import models
from .base import BaseModel
class Industry(BaseModel):

    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"