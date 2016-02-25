# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True)),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=75, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('lemail', models.TextField(null=True, blank=True)),
                ('school', models.TextField(null=True, blank=True)),
                ('grade', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set', blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('positionNO', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IdentifiedCharacter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField(null=True, blank=True)),
                ('hotspot_x', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('hotspot_y', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('hotspot_width', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('hotspot_height', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('side', models.TextField(null=True, blank=True)),
                ('lineNumber', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('filepath', models.TextField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('mimeType', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('imagePath', models.TextField(null=True, blank=True)),
                ('history', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='line',
            name='tablet',
            field=models.ForeignKey(to='homePage.Tablet', related_name='TabletNum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='identifiedcharacter',
            name='sign',
            field=models.ForeignKey(null=True, to='homePage.Sign', related_name='Sign', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='identifiedcharacter',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='Sign',
            field=models.ForeignKey(to='homePage.Sign', related_name='char_sign'),
            preserve_default=True,
        ),
    ]
