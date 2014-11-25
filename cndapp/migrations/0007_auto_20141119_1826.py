# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0006_auto_20141118_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eye',
            old_name='treated_eye',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gender',
            old_name='gender',
            new_name='name',
        ),
    ]
