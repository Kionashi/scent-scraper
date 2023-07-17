from django.db import models
from .base import BaseModel
class Family(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    parent = models.ForeignKey("Family", on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='perfumes/groups/')
    hero_image = models.ImageField(null=True, blank=True, upload_to='perfumes/groups/banners/')
    def __str__(self):
        return f"{self.name}"