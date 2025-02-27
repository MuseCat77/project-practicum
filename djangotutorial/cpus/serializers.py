from rest_framework import serializers
from cpus.models import Product

class CpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'product', 'type', 'release_date', 
            'foundry', 'vendor', 'process_size', 
            'tdp', 'die_size', 'transistors', 'freq',
            'fp16_gflops', 'fp32_gflops', 'fp64_gflops'
        ]
