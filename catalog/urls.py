from django.urls import path

from catalog.views import index, index_contacts, index_products, product

urlpatterns = [
    path('', index),
    path('contacts/', index_contacts),
    path('products/', index_products),
    path('product/', product),
]
