import random
from celery import Celery
from fulfil.celery import app
from .models import MyFile, Products
import csv
from django.utils import timezone


@app.task(name='tasks.processfile')
def processfile(fileName):
    start_time = timezone.now()
    file_path = '/app/test-data-set.csv'
    with open(file_path, "r") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        products = []
        for row in data:
            product = Products(
                sku=row[0],
                name=row[1],
                active=row[2],
                description=row[3]
            )
            products.append(product)
            if len(products) > 5000:
                Products.objects.bulk_create(
                    products, ignore_conflicts=True)
                products = []
        if products:
            Products.objects.bulk_create(products, ignore_conflicts=True)
    end_time = timezone.now()
    return True
