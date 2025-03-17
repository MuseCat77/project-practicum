from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from cpus.models import Product
from cpus.serializers import CpusSerializer
from .renderers import CSVRenderer  # Импортируем CSV-рендерер

class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CpusSerializer
    renderer_classes = [JSONRenderer, CSVRenderer]  # Добавляем поддержку CSV