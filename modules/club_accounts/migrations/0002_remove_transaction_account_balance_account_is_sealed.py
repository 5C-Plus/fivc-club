# Generated by Django 4.2.17 on 2024-12-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='account_balance',
        ),
        migrations.AddField(
            model_name='account',
            name='is_sealed',
            field=models.BooleanField(default=False),
        ),
    ]
