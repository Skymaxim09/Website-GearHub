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