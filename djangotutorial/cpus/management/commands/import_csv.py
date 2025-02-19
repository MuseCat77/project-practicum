import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from cpus.models import Product

class Command(BaseCommand):
    help = 'Import products from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'data/dataset.csv'  # Укажите путь к CSV

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Обработка даты: если дата некорректная, ставим None
                date_str = row['Release Date'].strip() if row['Release Date'] else None
                try:
                    release_date = datetime.strptime(date_str, "%Y-%m-%d") if date_str and date_str.lower() not in ["n/a", "unknown", ""] else None
                except ValueError:
                    release_date = None  # Если дата некорректна, ставим None

                # Создание объекта в базе
                Product.objects.create(
                    product=row['Product'],
                    type=row['Type'],
                    release_date=release_date
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
