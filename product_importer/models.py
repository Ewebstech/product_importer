from django.db import models


class Products(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    active = models.CharField(max_length=5)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

    objects = models.Manager()


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False, upload_to='files/')
    description = models.CharField(null=True, max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    objects = models.Manager()
