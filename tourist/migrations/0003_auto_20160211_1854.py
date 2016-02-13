# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0002_auto_20160211_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tourist',
            field=models.ForeignKey(to='tourist.Tourist', blank=True),
        ),
    ]
