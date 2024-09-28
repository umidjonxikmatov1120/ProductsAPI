from rest_framework import generics
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import ProductsModel
from products.serializers import ProductsViewSerializer

class ProductListView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsCreateView(generics.CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsUpdateView(generics.UpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsRetrieveView(generics.RetrieveAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer

class ProductsDeleteView(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsViewSerializer
