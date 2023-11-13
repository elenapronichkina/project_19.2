from django.shortcuts import render

from catalog.models import Category


def index(request):
    return render(request, 'catalog/index.html')


def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone}: {message}')
    return render(request, 'catalog/index_contacts.html')


def base_products(request):
    return render(request, 'catalog/base_products.html')


def index_product(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'КАТАЛОГ'
    }
    return render(request, 'catalog/index_product.html', context)



