from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='default_home'),
    path('/<slug:category_slug>', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact_view, name='contact'),
]
