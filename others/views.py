from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Banner, Post
from .forms import ContactForm
from products.models import Product

def home(request, category_slug='ban-phim'):
    banners = Banner.objects.filter(is_active=True)
    posts = Post.objects.order_by('-created_at')[:4]

    featured_products = Product.objects.filter(category__slug=category_slug, is_featured=True)[:4]
    
    if not featured_products:
        featured_products = Product.objects.filter(category__slug='ban-phim', is_featured=True)[:4]
    
    context = {
        'current_slug': category_slug,
        'banners': banners,
        'posts': posts,
        'featured_products': featured_products,
    }
    
    return render(request, 'home.html', context)

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'post-list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post-detail.html', {'post': post})

def contact_view(request):
    bad_words = ['ăn cắp', 'tuồn kho', 'lừa đảo', 'hack', 'scam', 'fake', 'hàng giả']
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            name = data['name']
            email = data['email']
            messages.success(request, f'Cảm ơn {name} đã liên hệ. Email liên hệ của bạn: {email}')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})
