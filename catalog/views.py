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


def index_products(request):
    return render(request, 'catalog/index_products.html')

def product(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Каталог - наши продукты'
    }
    return render(request, 'catalog/product.html', context)