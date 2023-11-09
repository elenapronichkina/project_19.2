from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    # def handle_category(self, *args, **options):
    #     category_list = [
    #         {'name': 'рассылки', 'description': 'отправка одного уведомления большому количеству получателей'},
    #         {'name': 'телеграм боты', 'description': 'алгоритмы, которые помогают решать опреленные задачи'},
    #         {'name': 'полезные утилиты', 'description': 'вспомогательные компьютерные программы для выполнения специализированных типовых задач'},
    #         {'name': 'веб-приложения', 'description': 'программное обеспечение или программа, которую можно открыть с помощью любого браузера'},
    #         {'name': 'микросервисы', 'description': 'сервисы для выполнения одной логической задачи'},
    #     ]
    #
    #     categories_for_create = []
    #     for category_item in category_list:
    #         categories_for_create.append(
    #             Category(**category_item)
    #         )
    #
    #     Category.objects.bulk_create(categories_for_create)
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Email рассылка', 'category': 'рассылки', 'description': 'Письмо, отправленное большому количеству получателей с целью продвижения бизнеса',
             'price': '15000'},
            {'name': 'SMS рассылка', 'category': 'рассылки', 'description': 'Сообщение о скидках, акциях, подтверждении заказа или доставки, отправленное на номер телефона получателя',
             'price': '10000'},
            {'name': 'Web push рассылка', 'category': 'рассылки',
             'description': 'Браузерные уведомления, которые видны пользователю даже при закрытом браузере',
             'price': '20000'},
            {'name': 'Рассылка в месседжеры', 'category': 'рассылки',
             'description': 'Сообщение, отправленное в Telegram, Facebook Messenger, Viber, в которое можно добавить текст, картинки, ссылку на сайт и кнопку',
             'price': '25000'},
            {'name': 'чат-боты', 'category': 'телеграм боты',
             'description': 'отвечают на вопросы клиентов и помогают им решать задачи',
             'price': '10000'},
            {'name': 'боты-инструменты', 'category': 'телеграм боты',
             'description': 'выполняют сложные функции: перевод, загрузка файлов, обучение',
             'price': '30000'},
            {'name': 'информационные боты', 'category': 'телеграм боты',
             'description': 'боты с полезной информацией, хранят базу, делают подборку',
             'price': '30000'},
            {'name': 'SPA', 'category': 'веб-приложения',
             'description': 'одностраничное интерактивное приложение',
             'price': '10000'},

        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
