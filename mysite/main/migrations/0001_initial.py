# Generated by Django 4.0.3 on 2023-11-08 01:13

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coffee",
            fields=[
                ('CoffeeID', models.IntegerField(primary_key=True, serialize=False)),
                ('NewID', models.IntegerField(unique=True)),
                ('CoffeeName', models.CharField(max_length=50)),
                ('Info', models.CharField(max_length=3000)),
                ('CoffeeType', models.TextField()),
                ('RoastingPoint', models.TextField()),
                ('Sustainability', models.CharField(max_length=4)),
                ('CupNote', models.TextField()),
                ('Body', models.CharField(max_length=1)),
                ('Sourness', models.CharField(max_length=1)),
                ('Sweetness', models.CharField(max_length=1)),
                ('Bitterness', models.CharField(max_length=1)),
                ('Caffeine', models.CharField(max_length=1)),
                ('CoffeeInfo', models.TextField()),
                ('Country', models.TextField()),
                ('ProductType', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('ExpirationDate', models.TextField()),
                ('ManufacturingDate', models.TextField()),
                ('Capacity', models.TextField()),
                ('StorageMethod', models.TextField()),
                ('RawMaterial', models.TextField()),
                ('ProductInfo', models.TextField()),
                ('Price', models.IntegerField()),
            ],
            options={
                "db_table": "coffee",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ('CustomerID', models.CharField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(8, '8자 이상으로 적어주세요!')])),
                ('name', models.CharField(max_length=8)),
                ('CustomerAddress', models.CharField(max_length=3000)),
                ('Gender', models.CharField(choices=[('F', '여성'), ('M', '남성')], max_length=1, null=True)),
                ('BirthDate', models.DateTimeField(default=datetime.date)),
                ('email', models.EmailField(max_length=40)),
                ('Password', models.TextField(validators=[django.core.validators.MinLengthValidator(8, '8자 이상으로 적어주세요!')])),
                ('PhoneNumber', models.TextField(validators=[django.core.validators.MinLengthValidator(10, '')])),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name="Roastery",
            fields=[
                ('RoasteryID', models.IntegerField(primary_key=True, serialize=False)),
                ('RoasteryName', models.CharField(max_length=45)),
                ('RoasteryAddress', models.CharField(max_length=3000)),
                ('RoasteryInfo', models.TextField()),
                ('RoasteryPhone', models.TextField(validators=[django.core.validators.MinLengthValidator(9, '')])),
            ],
            options={
                "db_table": "roastery",
            },
        ),
        migrations.CreateModel(
            name='test_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
                ('Caffeine', models.CharField(max_length=1)),
                ('CoffeeType', models.TextField()),
                ('CupNoteCategories', models.PositiveSmallIntegerField()),
                ('Body', models.CharField(max_length=1)),
                ('Sourness', models.CharField(max_length=1)),
                ('Sweetness', models.CharField(max_length=1)),
                ('Bitterness', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'mockuserinfo',
            },
        ),
        migrations.CreateModel(
            name='test_Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
                ('Stars', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField()),
                ('CoffeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coffee')),
            ],
            options={
                'db_table': 'mockreview',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('CoffeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coffee')),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.IntegerField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField()),
                ('OrderDate', models.DateTimeField()),
                ('CoffeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coffee')),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
            options={
                "db_table": "order",
            },
        ),
        migrations.AddField(
            model_name="coffee",
            name="RoasteryID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.roastery"
            ),
        ),
    ]
