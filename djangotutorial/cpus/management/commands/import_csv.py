import csv
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from cpus.models import Product
class Command(BaseCommand):
    help = "Импорт данных из CSV-файла в модель Product"

    # python manage.py import_csv "./data/dataset.csv"
    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Путь к CSV-файлу")

    def handle(self, *args, **options):
        file_path = options["file_path"]

        def parse_value(value, field_type):
            """ Преобразует строковые значения из CSV в нужные типы или None, если значение пустое """
            if value in ("", "NULL", "None", "NaT"):  # Проверка на пустые значения
                return None
            if field_type == int:
                return int(float(value))  # Исправленный вариант: сначала float, потом int
            if field_type == float or field_type == Decimal:
                return Decimal(value)
            if field_type == datetime.date:
                return datetime.strptime(value, "%Y-%m-%d").date()
            return value

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            products = []  # Список объектов для массового создания

            for row in reader:
                product = Product(
                    product=row["product"],
                    type=row["type"],
                    release_date=parse_value(row["release_date"], datetime.date),
                    process_size=parse_value(row["process_size"], int),
                    tdp=parse_value(row["tdp"], int),
                    die_size=parse_value(row["die_size"], Decimal),
                    transistors=parse_value(row["transistors"], int),
                    freq=parse_value(row["freq"], int),
                    foundry=parse_value(row["foundry"], str),
                    vendor=parse_value(row["vendor"], str),
                    fp16_gflops=parse_value(row["fp16_gflops"], Decimal),
                    fp32_gflops=parse_value(row["fp32_gflops"], Decimal),
                    fp64_gflops=parse_value(row["fp64_gflops"], Decimal),
                )
                products.append(product)

            Product.objects.bulk_create(products)
            self.stdout.write(self.style.SUCCESS(f"Успешно импортировано {len(products)} записей из {file_path}"))

