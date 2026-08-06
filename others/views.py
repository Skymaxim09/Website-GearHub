from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Banner, Post
from .forms import ContactForm
from products.models import Category

def home(request):
    banners = Banner.objects.filter(is_active=True)
    posts = Post.objects.order_by('-created_at')[:4]

    featured_by_category = {}
    categories = Category.objects.filter(is_available=True)
    for cat in categories:
        featured_qs = cat.products.filter(is_featured=True, is_available=True).order_by('-created_at')[:4]
        featured_by_category[cat.slug] = featured_qs

    context = {
        'banners': banners,
        'featured_by_category': featured_by_category,
        'posts': posts,
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
            content = form.cleaned_data['content'] or ''
            lowered = content.lower()
            found = [w for w in bad_words if w in lowered]
            if found:
                form.add_error('content', 'Nội dung chứa từ ngữ không phù hợp.')
            else:
                messages.success(request, 'Cảm ơn bạn đã gửi liên hệ. Chúng tôi sẽ phản hồi sớm.')
                success = True
                form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})
