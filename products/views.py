from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .views_registry import CATEGORY_MAP

def product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    category_config = CATEGORY_MAP.get(category_slug)
    
    if category_config:
        TargetModel = category_config['model']
        allowed_fields = category_config['filter_fields']
        
        product_queryset = TargetModel.objects.filter(is_available=True)
    else:
        TargetModel = Product
        allowed_fields = []
        
        product_queryset = TargetModel.objects.filter(category=category, is_available=True)
        
    filter_kwargs = {}
    for field in allowed_fields:
        value = request.GET.get(field)
        if value:
            filter_kwargs[field] = value
            
    if filter_kwargs:
        product_queryset = product_queryset.filter(**filter_kwargs)
        
    filter_meta = []
    if category_config:
        for field_name in allowed_fields:
            model_field = TargetModel._meta.get_field(field_name)
            if model_field.choices:
                filter_meta.append({
                    'name': field_name,
                    'verbose_name': model_field.verbose_name or field_name.title(),
                    'choices': model_field.choices,
                    'current_value': request.GET.get(field_name, '')
                })
                
    context = {
        'products': product_queryset,
        'filter_meta': filter_meta,
    }
    
    return render(request, 'product-list.html', context)

def product_detail(request, category_slug, pk):
    category = get_object_or_404(Category, slug=category_slug)
    category_config = CATEGORY_MAP.get(category_slug)
    
    if category_config:
        TargetModel = category_config['model']
        detail_fields = category_config['filter_fields']
    else:
        TargetModel = Product
        detail_fields = []
        
    product = get_object_or_404(TargetModel, pk=pk)
    
    custom_specs = []
    for field_name in detail_fields:
        if not hasattr(product, field_name):
            continue
        
        model_field = TargetModel._meta.get_field(field_name)
        verbose_name = model_field.verbose_name or field_name.replace('_', ' ').title()
        
        display_func = f'get_{field_name}_display'
        if hasattr(product, display_func):
            display_value = getattr(product, display_func)()
        else: 
            display_value = getattr(product, field_name)
            
        if display_value is not None and display_value != '':
            custom_specs.append({
                'label': verbose_name,
                'value': display_value
            })
            
    context = {
        'product': product,
        'custom_specs': custom_specs,
    }
    
    return render(request, 'product-detail.html', context)
