# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0004_auto_20141107_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gender',
            old_name='name',
            new_name='gender',
        ),
    ]
