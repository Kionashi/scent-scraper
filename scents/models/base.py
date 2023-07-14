from django.db import models
from django.core.validators import MinValueValidator

class BaseModel(models.Model):

    # Custom field types
    class PositiveDecimalField(models.DecimalField):
        def __init__(self, *args, **kwargs):
            kwargs['validators'] = [MinValueValidator(0)]
            super().__init__(*args, **kwargs)
        class Meta:
            abstract = True

    # Generic attributes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True