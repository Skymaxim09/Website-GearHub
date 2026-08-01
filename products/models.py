from django.db import models

# Create your models here.

# Model Category (
    # name(tối đa 100 kí tự), 
    # slug(unique=True), 
    # is_available(mặc định là True)
    # )
# Model Product (
    # STATUS_CHOICES (available, 'Còn hàng'; 'out_of_stock', 'Hết hàng'; 'discontinued', 'Ngừng bán'),
    # Foreign Key tới Category, name là 'products',
    # name(tối đa 100 kí tự),
    # price(số nguyên),
    # description(có thể để trống),
    # image('products/'),
    # status(choices là STATUS_CHOICES, tối đa 20 kí tự, mặc định là 'available'),
    # is_available(mặc định là True),
    # is_featured(mặc định là False),
    # created_at(tự động điền)
    # )
# Status của Product nếu khó quá thì bỏ qua nha

#chưa có STATUS
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name