# Generated by Django 4.0.2 on 2022-02-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('active', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]