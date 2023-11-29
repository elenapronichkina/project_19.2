from django.db import models
from django.contrib.auth.models import User

NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    body = models.TextField(verbose_name='публикация')
    slug = models.SlugField(max_length=200)
    image = models.ImageField( upload_to='products/', verbose_name='изображение', **NULLABLE)
    date_of_create = models.DateTimeField(**NULLABLE, verbose_name='дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #status = models.CharField(max_length=100, verbose_name='признак публикации')
    #количество    просмотров.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'