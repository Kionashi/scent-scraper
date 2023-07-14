from django.db import models
from .base import BaseModel
class Country(BaseModel):

    name = models.CharField(max_length=100)
    flag = models.ImageField(null=True, blank=True, upload_to='countries/')
    def __str__(self):
        return f"{self.name}"