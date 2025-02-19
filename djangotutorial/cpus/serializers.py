from rest_framework import serializers
from cpus.models import Product

class CpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'Product', 'Type', 'Release Date']
