from django.db import models
from .base import BaseModel
class Note(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    group = models.ForeignKey("NoteGroup", on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='notes/')
    hero_image = models.ImageField(null=True, blank=True, upload_to='notes/banners/')
    def __str__(self):
        return f"{self.name}"