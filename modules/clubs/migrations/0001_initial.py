# Generated by Django 4.2.17 on 2024-12-29 13:02

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
            name='Club',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(
                    auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(
                    auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid1, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('intro', models.TextField(blank=True, default='')),
                ('picture', models.ImageField(
                    default=None, null=True, upload_to='')),
                ('birthday', models.DateField(default=None, null=True)),
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