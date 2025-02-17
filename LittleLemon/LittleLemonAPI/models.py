from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    is_delivery_crew = models.BooleanField(default=False)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return super().__str__()
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deliveries')
    status = models.IntegerField(choices=[(0, "Out for delivery"), (1, "Delivered")], default=0)