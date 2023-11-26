from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', PostCreateView.as view(), name='create'),
    path('', ..., name='list'),
    path('view/<int:pk>/', ..., name='view'),
    path('edit/<int:pk>/', ..., name='edit'),
    path('delete/<int:pk>/', ..., name='delete'),
]
