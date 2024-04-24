# Generated by Django 2.2.13 on 2024-04-23 12:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Filter_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(choices=[('1000 TO 10000', '1000 TO 10000'), ('10000 TO 20000', '10000 TO 20000'), ('20000 TO 30000', '20000 TO 30000'), ('30000 TO 40000', '30000 TO 40000'), ('40000 TO 50000', '40000 TO 50000'), ('50000 TO 60000', '50000 TO 60000')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(upload_to='Product_images')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=100)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=200)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 4, 23, 12, 33, 26, 316321, tzinfo=utc))),
                ('brands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Brand')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Categories')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Color')),
                ('filter_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Filter_Price')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product_images/img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.Product')),
            ],
        ),
    ]
