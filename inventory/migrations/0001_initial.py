# Generated by Django 5.0.6 on 2024-07-01 22:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Name must contain at least three alphanumeric characters (a-z, 0-9, _).', regex='^[a-z0-9_]{3,50}$')])),
                ('path', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='inventory.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('visible', models.BooleanField(default=False)),
                ('max_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='MRP')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Selling Price')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Amount')),
                ('executed_amount', models.DecimalField(decimal_places=3, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Executed Amount')),
                ('unit', models.CharField(choices=[('kg', 'Kg'), ('g', 'gram'), ('l', 'L'), ('ml', 'mL'), ('p', 'Pack')], max_length=5)),
                ('note', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='inventory.category')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store', to='inventory.store')),
            ],
            options={
                'verbose_name_plural': 'inventories',
            },
        ),
    ]
