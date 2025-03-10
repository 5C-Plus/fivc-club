# Generated by Django 4.2.17 on 2025-02-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        (
            'club_meetings',
            '0013_alter_meetingsessionrolebinding_unique_together'
        ),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={('club', 'name')},
        ),
    ]
