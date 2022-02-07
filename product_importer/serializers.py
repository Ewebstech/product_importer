from .models import Products, MyFile
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'sku', 'name', 'active',
                  'description', 'created', 'updated')


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFile
        fields = ('file', 'description', 'uploaded_at')
