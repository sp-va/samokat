import uuid

from django.db import models


class Product(models.Model):
    id: models.UUIDField = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name: models.CharField = models.CharField()
    description: models.TextField = models.TextField()
    shelf_life: models.IntegerField = models.IntegerField(default=None, null=True, blank=True)
    manufacturer: models.CharField = models.CharField()
