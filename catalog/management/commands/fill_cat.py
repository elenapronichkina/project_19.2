from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'рассылки', 'description': 'отправка одного уведомления большому количеству получателей'},
            {'name': 'телеграм боты', 'description': 'алгоритмы, которые помогают решать опреленные задачи'},
            {'name': 'полезные утилиты', 'description': 'вспомогательные компьютерные программы для выполнения специализированных типовых задач'},
            {'name': 'веб-приложения', 'description': 'программное обеспечение или программа, которую можно открыть с помощью любого браузера'},
            {'name': 'микросервисы', 'description': 'сервисы для выполнения одной логической задачи'},
        ]

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)