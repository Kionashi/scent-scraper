from django.db import models
from .base import BaseModel
class Perfume(BaseModel):
    class Categories(models.TextChoices):
        MAN = 'man'
        WOMAN = 'woman'
        UNISEX = 'unisex'

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    desginer = models.ForeignKey("Designer", on_delete=models.CASCADE)
    perfumists = models.ManyToManyField("Perfumist")
    accords = models.ManyToManyField("Accord",  through='PerfumeAccord', related_name='perfumes')
    ref_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='perfumes/')
    category = models.CharField(max_length=10, choices=Categories.choices, default=Categories.UNISEX)
    creation_year = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.name}"