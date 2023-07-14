from django.db import models
from .base import BaseModel

class Perfumer(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    company = models.CharField(max_length=100, blank=True,null=True)
    other_companies = models.CharField(max_length=100, blank=True,null=True)
    education = models.CharField(max_length=100, blank=True,null=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='perfumers/')
    def __str__(self):
        return f"{self.name}"