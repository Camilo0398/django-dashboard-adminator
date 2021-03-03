from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from app import models
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    # serializer_class = serializers.UserSerializers
    # queryset = models.User.objects.all()
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('accountemail', )

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('typeproduct_typeproductid','productid' )

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializers
    queryset = models.Company.objects.all()
