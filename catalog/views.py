from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index_product.html'

# def index_product(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'КАТАЛОГ'
#     }
#     return render(request, 'catalog/index_product.html', context)

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/product.html'
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product.html'
# def product(request, pk):
#     category = Category.objects.get(pk=pk)
#     data = {
#         'object_list': Product.objects.filter(category2=pk),
#         'title': f'продукты категории {category.name}',
#     }
#     return render(request, 'catalog/product.html', data)

