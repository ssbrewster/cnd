# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0005_auto_20141113_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eye',
            old_name='name',
            new_name='treated_eye',
        ),
    ]
