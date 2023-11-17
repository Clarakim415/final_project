# Generated by Django 4.2.7 on 2023-11-17 05:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("name", models.CharField(max_length=8)),
                ("CustomerAddress", models.CharField(max_length=3000, null=True)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("F", "여성"), ("M", "남성")], max_length=1, null=True
                    ),
                ),
                ("BirthDate", models.DateField(null=True)),
                (
                    "PhoneNumber",
                    models.TextField(
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10, "")],
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cart_id", models.CharField(blank=True, max_length=250)),
                ("date_added", models.DateField(auto_now_add=True)),
            ],
            options={
                "db_table": "Cart",
                "ordering": ["date_added"],
            },
        ),
        migrations.CreateModel(
            name="Coffee",
            fields=[
                ("CoffeeID", models.IntegerField(primary_key=True, serialize=False)),
                ("NewID", models.IntegerField(unique=True)),
                ("CoffeeName", models.CharField(max_length=50)),
                ("CoffeeType", models.TextField()),
                ("RoastingPoint", models.TextField()),
                ("Sustainability", models.CharField(max_length=4)),
                ("CupNote", models.TextField()),
                ("Body", models.CharField(max_length=1)),
                ("Sourness", models.CharField(max_length=1)),
                ("Sweetness", models.CharField(max_length=1)),
                ("Bitterness", models.CharField(max_length=1)),
                ("Caffeine", models.CharField(max_length=1)),
                ("CoffeeInfo", models.TextField()),
                ("Country", models.TextField()),
                ("ProductType", models.TextField()),
                ("Manufacturer", models.TextField()),
                ("ExpirationDate", models.TextField()),
                ("ManufacturingDate", models.TextField()),
                ("Capacity", models.TextField()),
                ("StorageMethod", models.TextField()),
                ("RawMaterial", models.TextField()),
                ("ProductInfo", models.TextField()),
                ("Price", models.IntegerField()),
                ("Stock", models.IntegerField()),
                ("Created_date", models.DateField()),
            ],
            options={
                "db_table": "coffee",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "OrderID",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("emailAddress", models.EmailField(blank=True, max_length=250)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "coffee_order",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Roastery",
            fields=[
                ("RoasteryID", models.IntegerField(primary_key=True, serialize=False)),
                ("RoasteryName", models.CharField(max_length=45)),
                ("RoasteryAddress", models.CharField(max_length=3000)),
                ("RoasteryInfo", models.TextField()),
                (
                    "RoasteryPhone",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(9, "")]
                    ),
                ),
            ],
            options={
                "db_table": "roastery",
            },
        ),
        migrations.CreateModel(
            name="test_preference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=40)),
                ("Caffeine", models.CharField(max_length=1)),
                ("CoffeeType", models.TextField()),
                ("CupNoteCategories", models.TextField()),
                ("Body", models.CharField(max_length=1)),
                ("Sourness", models.CharField(max_length=1)),
                ("Sweetness", models.CharField(max_length=1)),
                ("Bitterness", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "mockuserinfo",
            },
        ),
        migrations.CreateModel(
            name="test_Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=40)),
                ("Stars", models.IntegerField(default=0)),
                ("created_date", models.DateTimeField()),
                (
                    "CoffeeID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.coffee"
                    ),
                ),
            ],
            options={
                "db_table": "mockreview",
            },
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(default="", max_length=4)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("payDate", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField()),
                (
                    "CoffeeID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.coffee"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "review",
            },
        ),
        migrations.CreateModel(
            name="Preference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caf", models.CharField(default="", max_length=1)),
                ("blend", models.CharField(default="", max_length=1)),
                ("notes", models.TextField(default="")),
                ("sour", models.CharField(default="", max_length=1)),
                ("sweet", models.CharField(default="", max_length=1)),
                ("bitter", models.CharField(default="", max_length=1)),
                ("body", models.CharField(default="", max_length=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("quantity", models.IntegerField()),
                (
                    "OrderID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_id",
                        to="main.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.coffee"
                    ),
                ),
            ],
            options={
                "db_table": "OrderItem",
            },
        ),
        migrations.AddField(
            model_name="coffee",
            name="RoasteryID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.roastery"
            ),
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("active", models.BooleanField(default=True)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.coffee"
                    ),
                ),
            ],
            options={
                "db_table": "CartItem",
            },
        ),
    ]
