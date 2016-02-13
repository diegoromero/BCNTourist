# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_number', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=128, blank=True)),
                ('last_name', models.CharField(default=b'', max_length=128, blank=True)),
                ('passport', models.CharField(default=b'', max_length=20, blank=True)),
                ('email', models.EmailField(default=b'', max_length=64, blank=True)),
                ('telephone', models.CharField(default=b'', max_length=20, blank=True)),
                ('country', models.CharField(default=b'', max_length=64, blank=True)),
                ('city', models.CharField(default=b'', max_length=64, blank=True)),
                ('state', models.CharField(default=b'', max_length=64, blank=True)),
                ('zip_code', models.CharField(default=b'', max_length=10, blank=True)),
                ('street_address', models.CharField(default=b'', max_length=255, blank=True)),
                ('lat', models.CharField(max_length=30)),
                ('lon', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='tourist',
            field=models.ForeignKey(to='tourist.Tourist'),
        ),
    ]
