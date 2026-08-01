from django.contrib import admin
from .models import OrderItem, Order

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'phone', 'status', 'get_total_order')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'email', 'phone', 'address')
    readonly_fields = ('user', 'email', 'get_total_order', 'created_at')
    inlines = [OrderItemInLine]
    fieldsets = (
        ('Thông tin khách hàng', {'fields': ('user', 'email', 'phone', 'address')}),
        ('Ghi chú & Trạng thái đơn hàng', {'fields': ('notes', 'status')}),
        ('Thông tin đơn hàng', {
            'fields': ('created_at', 'get_total_order'),
            'classes': ['collapse']}),
    )
    
    def get_total_order(self, obj):
        return f'{obj.total_order():,} đ'
    get_total_order.short_descriptions = 'Tổng tiền'
    