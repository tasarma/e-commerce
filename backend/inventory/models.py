from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from users.models import CustomUser
from tenant.models import TenantAwareModel

class Product(TenantAwareModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="media", default="")
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    is_on_sale = models.BooleanField(default=False)
    expire_date = models.DateField(default=date.today)
    contents = models.TextField(default="")

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if not self.image:
            raise ValidationError("Lütfen bir fotoğraf yükleyin!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 270 and h != 370:
                raise ValidationError("Fotoğraf 270 x 370 boyutunda olmalıdır!")


class ProductSpesifications(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=4000)

    def __str__(self):
        return f"{self.product.name}'s settings"


class ProductOrderingInformations(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    material = models.CharField(max_length=20)
    description = models.CharField(max_length=4000)
    packaging = models.CharField(max_length=4000)

    def __str__(self):
        return f"{self.product.name}'s settings"

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    paymentMethod =  models.CharField(max_length=200, null=True, blank=True)
    taxPrice =  models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False) 

    def __str__(self):
        return str(self.createdAt)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name =  models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    _id = models.AutoField(primary_key=True,editable=False) 
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True,editable=False) 

    def __str__(self):
        return str(self.address)

