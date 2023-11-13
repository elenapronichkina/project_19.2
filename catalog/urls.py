from django.urls import path

from catalog.views import index, index_contacts, base_products, index_product

urlpatterns = [
    path('', index),
    path('contacts/', index_contacts),
    path('products/', index_product),
    path('product/', base_products),
]
