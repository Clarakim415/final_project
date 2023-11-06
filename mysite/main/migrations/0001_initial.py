# Generated by Django 4.0.3 on 2023-11-01 05:48

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('CoffeeID', models.IntegerField(primary_key=True, serialize=False)),
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
            ],
            options={
                'db_table': 'coffee',
            },
        ),
        migrations.CreateModel(
            name='Customer',
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
        ),
        migrations.CreateModel(
            name='Roastery',
            fields=[
                ('RoasteryID', models.IntegerField(primary_key=True, serialize=False)),
                ('RoasteryName', models.CharField(max_length=45)),
                ('RoasteryAddress', models.CharField(max_length=3000)),
                ('RoasteryInfo', models.TextField()),
            ],
            options={
                'db_table': 'roastery',
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
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='coffee',
            name='RoasteryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roastery'),
        ),
    ]
