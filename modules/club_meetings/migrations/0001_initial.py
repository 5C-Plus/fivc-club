# Generated by Django 4.2.17 on 2025-01-10 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0001_initial'),
        ('club_members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
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
                ('date',
                 models.DateField()),
                ('time',
                 models.TimeField()),
                ('theme',
                 models.TextField(
                     blank=True,
                     default='')),
                ('extra',
                 models.TextField(
                     blank=True,
                     default='')),
                ('club',
                 models.ForeignKey(
                     db_constraint=False,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meetings',
                     to='clubs.club')),
                ('created_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
                ('meeting_manager',
                 models.ForeignKey(
                     db_constraint=False,
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meetings',
                     to='club_members.attendee')),
                ('modified_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingVenue',
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
                ('address',
                 models.TextField()),
                ('extra',
                 models.URLField(
                     default=None,
                     null=True)),
                ('club',
                 models.ForeignKey(
                     db_constraint=False,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meeting_venues',
                     to='clubs.club')),
                ('created_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
                ('modified_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingSession',
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
                ('name',
                 models.CharField(
                     max_length=255)),
                ('order',
                 models.FloatField()),
                ('duration',
                 models.DurationField()),
                ('created_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
                ('meeting',
                 models.ForeignKey(
                     db_constraint=False,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meeting_sessions',
                     to='club_meetings.meeting')),
                ('modified_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingRole',
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
                ('type',
                 models.CharField(
                     choices=[
                         ('TME',
                          'Toastmaster Of the Evening'),
                         ('TMD',
                          'Toastmaster Of the Day'),
                         ('TTM',
                          'Table Topics Master'),
                         ('IE',
                          'Individual Evaluator'),
                         ('GE',
                          'General Evaluator'),
                         ('Timer',
                          'Timer'),
                         ('AhCounter',
                          'Ah Counter'),
                         ('Grammarian',
                          'Grammarian'),
                         ('Photographer',
                          'Photographer'),
                         ('ItSupport',
                          'IT Support'),
                         ('SharingMaster',
                          'Sharing Master'),
                         ('ContestChair',
                          'Contest Chair'),
                         ('ElectionChair',
                          'Election Chair'),
                         ('BallotCounter',
                          'Ballot Counter'),
                         ('SAA',
                          'Sergeant At Arms')],
                     max_length=32)),
                ('attendee',
                 models.ForeignKey(
                     db_constraint=False,
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meeting_roles',
                     to='club_members.attendee')),
                ('created_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
                ('meeting',
                 models.ForeignKey(
                     db_constraint=False,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='meeting_roles',
                     to='club_meetings.meeting')),
                ('meeting_session',
                 models.ForeignKey(
                     db_constraint=False,
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='meeting_roles',
                     to='club_meetings.meetingsession')),
                ('modified_by',
                 models.ForeignKey(
                     db_constraint=False,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='+',
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='meeting',
            name='venue',
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='meetings',
                to='club_meetings.meetingvenue'),
        ),
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={
                (
                    'club',
                    'date')},
        ),
    ]