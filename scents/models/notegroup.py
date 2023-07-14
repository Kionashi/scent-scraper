from django.db import models
from .base import BaseModel
class NoteGroup(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    hero_image = models.ImageField(null=True, blank=True, upload_to='notes/groups/')
    def __str__(self):
        return f"{self.name}"