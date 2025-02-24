from django.db import models

class Product(models.Model):
    product = models.CharField(max_length=200, verbose_name="Название продукта")
    type = models.CharField(max_length=3, verbose_name="Тип")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата выпуска")

    foundry = models.CharField(max_length=100, null=True, blank=True, verbose_name="Производитель (Foundry)")
    vendor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Бренд (Vendor)")

    process_size = models.IntegerField(null=True, blank=True, verbose_name="Техпроцесс (нм)")
    tdp = models.IntegerField(null=True, blank=True, verbose_name="TDP (Вт)")
    die_size = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Размер кристалла (мм²)")
    transistors = models.IntegerField(null=True, blank=True, verbose_name="Транзисторы (млн)")
    freq = models.IntegerField(null=True, blank=True, verbose_name="Частота (МГц)")
    
    fp16_gflops = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="FP16 GFLOPS")
    fp32_gflops = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="FP32 GFLOPS")
    fp64_gflops = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="FP64 GFLOPS")


    class Meta:
        db_table = "cpus_products"  # Задаёт имя таблицы (необязательно)
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"

    def __str__(self):
        return self.product
