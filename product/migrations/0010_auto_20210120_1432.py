# Generated by Django 3.1.4 on 2021-01-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210120_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
