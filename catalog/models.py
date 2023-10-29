from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

def __str__(self):
    return f'{self.name}'

class Meta:
    verbose_name = 'категория'
    verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    picture = models.ImageField( upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.PositiveIntegerField (verbose_name='Цена за покупку')
    date_of_create = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_change = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата последнего изменения')


    def __str__(self):
        return f'{self.name} ({self.category}) {self.description} {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
