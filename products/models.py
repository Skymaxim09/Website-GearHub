from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class StatusChoice(models.TextChoices):
        IN_STOCK = 'in_stock', 'Còn hàng'
        WARNING_STOCK = 'warning_stock', 'Sắp hết hàng'
        OUT_OF_STOCK = 'out_of_stock', 'Hết hàng'
        DISCONTINUED = 'discontinued', 'Ngừng bán'
        
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    quantity = models.PositiveIntegerField(default=0)
    
    status = models.CharField(
        max_length=20, 
        choices=StatusChoice.choices, 
        default=StatusChoice.IN_STOCK)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.is_featured or not self.category_id:
            return
        
        featured_query = Product.objects.filter(
            is_featured=True, category=self.category_id
        )
        
        if self.pk:
            featured_query = featured_query.exclude(pk=self.pk)
        
        if featured_query >= 4:
            raise ValidationError(
                'Chỉ tối đa 4 sản phẩm nổi bật mỗi danh mục sản phẩm'
            )
    
    def save(self, *args, **kwargs):
        self.full_clean()
        
        discontinued = self.StatusChoice.DISCONTINUED
        
        # Check available to add status
        if self.is_available == False:
            self.status = discontinued
        else: self.status = self.StatusChoice.IN_STOCK
        
        # Check available to switch featured
        if self.is_available == False and self.status == discontinued:
            self.is_featured = False
            
        # Check quantity to add status
        if self.status != discontinued:
            if self.quantity == 0:
                self.status = self.StatusChoice.OUT_OF_STOCK
            elif 0 < self.quantity <= 5:
                self.status = self.StatusChoice.WARNING_STOCK
            else:
                self.status = self.StatusChoice.IN_STOCK
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Keyboard(Product):
    class Layout(models.TextChoices):
        LAYOUT_65 = 'layout_65', 'Layout 65%'
        LAYOUT_75 = 'layout_75', 'Layout 75%'
        FULL_LAYOUT = 'layout_100', 'Layout Fullsize'
        
    class KeyboardType(models.TextChoices):
        MECH = 'mech', 'Bàn phím cơ'
        HE = 'he', 'Bàn phím HE'
        LOW_PROFILE = 'low_profile', 'Bàn phím Low Profile'
    
    class Connection(models.TextChoices):
        WIRED = 'wired', 'có dây'
        WIRELESS = 'wireless', 'không dây'
        
    layout = models.CharField(max_length=15, choices=Layout.choices, verbose_name="Layout")
    keyboard_type = models.CharField(max_length=20, choices=KeyboardType.choices, verbose_name="Loại bàn phím")
    connection = models.CharField(max_length=15, choices=Connection.choices, verbose_name="Kiểu kết nối")

class Switch(Product):
    class SwitchType(models.TextChoices):
        LINEAR = 'linear', 'Linear'
        TACTILE = 'tactile', 'Tactile'
        SLIENT = 'slient', 'Slient'
        HE = 'he', 'HE'
        
    switch_type = models.CharField(max_length=15, choices=SwitchType.choices, verbose_name="Loại switch")

class Keycap(Product):
    class Profile(models.TextChoices):
        CHERRY = 'cherry', 'Cherry'
        XDA = 'xda', 'XDA'
        MOA = 'moa', 'MOA'
        ARTISAN = 'artisan', 'Artisan'
    
    class Material(models.TextChoices):
        PBT = 'pbt', 'PBT'
        ABS = 'abs', 'ABS'
    
    class PrintTech(models.TextChoices):
        DOUBLE_SHOT = 'double_shot', 'Doubleshot'
        DYE_SUB = 'dye_sub', 'Dyesub'
        
    profile = models.CharField(max_length=10, choices=Profile.choices, verbose_name="Profile")
    material = models.CharField(max_length=5, choices=Material.choices, verbose_name="Chất liệu")
    print_tech = models.CharField(max_length=15, choices=PrintTech.choices, verbose_name="Công nghệ in")

class Mouse(Product):
    class Connection(models.TextChoices):
        WIRED = 'wired', 'có dây'
        WIRELESS = 'wireless', 'không dây'
        
    class Brand(models.TextChoices):
        LOGITECH = 'logitech', 'Logitech'
        RAZER = 'razer', 'Razer'
        GRAVASTAR = 'gravastar', 'Gravastar'
        OTHERS = 'others', 'Khác'
        
    class MouseType(models.TextChoices):
        OFFICE = 'office', 'Văn phòng' 
        GAMMING = 'gamming' 'Gamming'
        
    connection = models.CharField(max_length=15, choices=Connection.choices, verbose_name="Kiểu kết nối")
    brand = models.CharField(max_length=15, choices=Brand.choices, verbose_name="Thương hiệu")
    mouse_type = models.CharField(max_length=15, choices=MouseType.choices, verbose_name="Thể loại")

class ModTool(Product):
    class MTType(models.TextChoices):
        TOOLS = 'tools', 'Dụng cụ mod'
        LUBE = 'lube', 'Mỡ lube'
        MODDING = 'modding', 'Vật liệu mod'
        
    mt_type = models.CharField(max_length=20, choices=MTType.choices, verbose_name="Thể loại")
    