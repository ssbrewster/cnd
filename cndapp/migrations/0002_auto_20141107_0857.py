# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opnote',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preopassessment',
            name='keratomy_unit',
            field=models.ForeignKey(verbose_name=b'Keratometry unit', to='cndapp.KeratomyUnit'),
            preserve_default=True,
        ),
    ]
