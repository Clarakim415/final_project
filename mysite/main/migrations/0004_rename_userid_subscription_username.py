# Generated by Django 4.2.7 on 2023-11-14 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subscription_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='userID',
            new_name='userName',
        ),
    ]
