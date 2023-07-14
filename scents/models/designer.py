from django.db import models
from .base import BaseModel
class Designer(BaseModel):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE,null=True, blank=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE,null=True, blank=True)
    parent_company = models.ForeignKey("ParentCompany", on_delete=models.CASCADE, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to='designers/')
    def __str__(self):
        return f"{self.name}"