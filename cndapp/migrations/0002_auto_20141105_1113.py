# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opnote',
            name='first_eye',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opnote',
            name='lens_inserted',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='able_to_cooperate',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='able_to_lie_flat',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='alpha_blockers',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='diabetes',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='guarded_prognosis',
            field=models.BooleanField(default=None, choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
    ]
