from django.shortcuts import render
from rest_framework import status
from rest_framework.views import View, APIView
from .serializers import ProductsSerializer, MyFileSerializer
from .models import MyFile, Products
from django.http import JsonResponse
from django import forms
import csv
from django.utils import timezone
import logging
from .tasks import *
from rest_framework.response import Response
from django.http.response import Http404
from django.core.paginator import Paginator


class ProductsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Products.objects.all()
        paginator = Paginator(data, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = ProductsSerializer(page_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = ProductsSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Product Added Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        products_to_update = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(
            instance=products_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Product Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        products_to_delete = Products.objects.get(pk=pk)

        products_to_delete.delete()

        return Response({
            'message': 'Products Deleted Successfully'
        })


class ImportFileForm(forms.Form):
    file = forms.FileField()


class MyFileView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ImportFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["file"]
                # Write the file to disk
                fileName = csv_file.name
                fout = open(fileName, 'wb')
                for chunk in csv_file.chunks():
                    fout.write(chunk)
                fout.close()
                # Push to background
                processfile.delay(fileName)
                data = {
                    'status': status.HTTP_201_CREATED,
                    'message': 'Successful Upload'
                }
                return JsonResponse(data)
