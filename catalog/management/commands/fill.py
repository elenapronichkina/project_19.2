from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'холодильник Атлант', 'category': 'крупная бытовая техника', 'description': 'no frost',
             'price': '25000'},
            {'name': 'газовая плита Zanussi', 'category': 'крупная бытовая техника', 'description': '4 комфорки',
             'price': '20000'},
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
