from django.urls import path
from . import views

urlpatterns = [
    path('search-product/', views.search, name='search_box'),
    path('product-list--<slug:category_slug>/', views.product_list, name='product_list'),
    path('product-detail--<slug:category_slug>/<int:pk>/', views.product_detail, name='product_detail'),
]
