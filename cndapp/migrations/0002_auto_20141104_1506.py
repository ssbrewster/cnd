# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUpVisualAcuityReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=3, decimal_places=2)),
                ('correction', models.ForeignKey(to='cndapp.VisualAcuityCorrection')),
                ('eye', models.ForeignKey(to='cndapp.Eye')),
                ('followup', models.ForeignKey(to='cndapp.FollowUp')),
                ('scale', models.ForeignKey(to='cndapp.VisualAcuityScale')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreOpAssessmentVisualAcuityReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=3, decimal_places=2)),
                ('correction', models.ForeignKey(to='cndapp.VisualAcuityCorrection')),
                ('eye', models.ForeignKey(to='cndapp.Eye')),
                ('preopassessment', models.ForeignKey(to='cndapp.PreOpAssessment')),
                ('scale', models.ForeignKey(to='cndapp.VisualAcuityScale')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='visualacuityreading',
            name='correction',
        ),
        migrations.RemoveField(
            model_name='visualacuityreading',
            name='eye',
        ),
        migrations.RemoveField(
            model_name='visualacuityreading',
            name='scale',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='visual_acuity',
        ),
        migrations.RemoveField(
            model_name='preopassessment',
            name='visual_acuity',
        ),
        migrations.DeleteModel(
            name='VisualAcuityReading',
        ),
    ]
