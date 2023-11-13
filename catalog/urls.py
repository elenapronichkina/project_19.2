from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, index_contacts, base_products, index_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', index_contacts),
    path('products/', index_product, name='index_product'),
    path('product/', base_products),
]
