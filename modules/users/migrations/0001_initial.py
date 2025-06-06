# Generated by Django 4.2.17 on 2025-04-15 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created_time',
                 models.DateTimeField(
                     auto_now_add=True,
                     db_index=True)),
                ('modified_time',
                 models.DateTimeField(
                     auto_now=True,
                     db_index=True)),
                ('uuid',
                 models.UUIDField(
                     default=uuid.uuid1,
                     unique=True)),
                ('content',
                 models.JSONField(
                     default=dict)),
                ('user',
                 models.OneToOneField(
                     db_constraint=False,
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='preference',
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
