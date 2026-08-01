from django.db import models
from django.conf import settings

# Create your models here.

class StatusChoices(models.TextChoices):
    pending = 'pending', 'Chờ duyệt'
    approved = 'approved', 'Đã duyệt'
    cancelled = 'cancelled' 'Đã hủy'
    delivery = 'delivery', 'Đang giao'
    delivered = 'delivered', 'Đã nhận'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(unique=False, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    address = models.TextField(max_length=500, blank=False)
    notes = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_order(self):
        return sum(item.total_item() for item in self.items.all())
    
    def __str__(self):
        return f'Order #{self.id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_item(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'Item {self.product}: {self.order}'