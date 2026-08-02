from django.contrib import admin
from .models import Category, Keyboard, Switch, Keycap, Mouse, ModTool

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'is_available')
    list_filter = ['is_available']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
    
class BaseProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'get_status_display', 'is_featured')
    list_filter = ('status', 'is_featured')
    search_fields = ('name', 'price')
    readonly_fields = ('status', 'created_at')
    fieldsets = (
        ('Thông tin sản phẩm', {
            'fields': ('name', 'category', 'price', 'description', 'image', 'quantity', 'created_at')}),
        ('Trạng thái sản phẩm', {
            'fields': ('status', 'is_available', 'is_featured'),
            'description': 'Trạng thái(Status) sẽ tự động cập nhật'}),
    )
    
@admin.register(Keyboard)
class KeyboardAdmin(BaseProductAdmin):
    list_filter = BaseProductAdmin.list_filter + (
        'layout', 'switch_type', 'connection')
    fieldsets = BaseProductAdmin.fieldsets + (
        ('Phân loại sản phẩm', {'fields': ('layout', 'switch_type', 'connection')}),
    )
    
@admin.register(Switch)
class SwitchAdmin(BaseProductAdmin):
    list_filter = BaseProductAdmin.list_filter + (
        's_type',)
    fieldsets = BaseProductAdmin.fieldsets + (
        ('Phân loại sản phẩm', {'fields': ('s_type',)}),
    )

@admin.register(Keycap)
class KeycapAdmin(BaseProductAdmin):
    list_filter = BaseProductAdmin.list_filter + (
        'profile', 'material', 'print_tech')
    fieldsets = BaseProductAdmin.fieldsets + (
        ('Phân loại sản phẩm', {'fields': ('profile', 'material', 'print_tech')}),
    )
    
@admin.register(Mouse)
class MouseAdmin(BaseProductAdmin):
    list_filter = BaseProductAdmin.list_filter + (
        'connection', 'brand', 'mouse_type')
    fieldsets = BaseProductAdmin.fieldsets + (
        ('Phân loại sản phẩm', {'fields': ('connection', 'brand', 'mouse_type')}),
    )
    
@admin.register(ModTool)
class ModToolAdmin(BaseProductAdmin):
    list_filter = BaseProductAdmin.list_filter + (
        'mt_type',)
    fieldsets = BaseProductAdmin.fieldsets + (
        ('Phân loại sản phẩm', {'fields': ('mt_type',)}),
    )