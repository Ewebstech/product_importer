# Generated by Django 4.0.2 on 2022-02-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_importer', '0004_alter_myfile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
    ]