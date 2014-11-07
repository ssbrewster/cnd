# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0002_auto_20141107_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followuprefraction',
            name='axis',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(180)]),
            preserve_default=True,
        ),
    ]
