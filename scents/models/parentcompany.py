from django.db import models
from .base import BaseModel
class ParentCompany(BaseModel):

    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"