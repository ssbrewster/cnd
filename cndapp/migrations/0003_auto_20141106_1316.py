# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0002_auto_20141105_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preopassessment',
            name='iol_power',
            field=models.DecimalField(verbose_name=b'IOL power', max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='morphology',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
