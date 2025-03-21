# Generated by Django 4.2.17 on 2025-01-27 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(
                    auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(
                    auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid1, unique=True)),
                ('name', models.CharField(default='default', max_length=64)),
                ('description', models.TextField(blank=True, default='')),
                ('is_sealed', models.BooleanField(default=False)),
                ('club', models.ForeignKey(
                    db_constraint=False,
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='accounts', to='clubs.club')),
                ('created_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('club', 'name')},
            },
        ),
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(
                    auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(
                    auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(
                    default=uuid.uuid1, unique=True)),
                ('name', models.CharField(
                    default='default', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('club', models.ForeignKey(
                    db_constraint=False, default=None, null=True,
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='transaction_categories', to='clubs.club')),
                ('created_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(
                    auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(
                    auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid1, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('transact_amount', models.DecimalField(
                    decimal_places=2, max_digits=12)),
                ('transact_audited', models.BooleanField(default=False)),
                ('transact_time', models.DateTimeField()),
                ('account', models.ForeignKey(
                    db_constraint=False,
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='transactions',
                    to='club_accounts.account')),
                ('category', models.ForeignKey(
                    db_constraint=False, default=None, null=True,
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='transactions',
                    to='club_accounts.transactioncategory')),
                ('created_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(
                    db_constraint=False, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
