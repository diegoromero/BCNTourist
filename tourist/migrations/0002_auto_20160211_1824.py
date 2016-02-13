# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='lat',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='lon',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
    ]
