# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_character_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssyrianChar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('line', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('positionNO', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('Sign', models.ForeignKey(to='homePage.Sign', related_name='char_sign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='character',
            name='Sign',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
    ]
