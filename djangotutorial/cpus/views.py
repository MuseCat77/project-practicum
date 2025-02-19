from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from cpus.models import Product
from cpus.serializers import CpusSerializer

# Список вопросов
class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = CpusSerializer
