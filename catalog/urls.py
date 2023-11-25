from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, index_contacts, ProductListView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', index_contacts),
    path('products/', ProductListView.as_view(), name='index_product'),
    path('product/<int:pk>/', CategoryListView.as_view(), name='product'),
]
