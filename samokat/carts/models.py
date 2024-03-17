import uuid

from django.db import models

from products.models import Product
from users.models import User

class OrderCart(models.Model):
    id: models.UUIDField = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    owner: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    products: models.ManyToManyField = models.ManyToManyField(Product)

