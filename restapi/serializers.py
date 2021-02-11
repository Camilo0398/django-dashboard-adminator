from rest_framework import serializers
from app import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'