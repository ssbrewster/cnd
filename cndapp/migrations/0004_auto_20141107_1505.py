# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0003_auto_20141107_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opnote',
            name='age',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
