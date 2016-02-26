# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_auto_20160222_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='assyrianchar',
            name='Tablet',
            field=models.ForeignKey(default=1, related_name='char_sign', to='homePage.Tablet'),
            preserve_default=False,
        ),
    ]
