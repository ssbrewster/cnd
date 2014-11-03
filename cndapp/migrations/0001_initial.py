# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('iso', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostcodeValidator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pattern', models.CharField(max_length=64)),
                ('error', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='country',
            name='postcode_validator',
            field=models.ForeignKey(to='cndapp.PostcodeValidator'),
            preserve_default=True,
        ),
    ]
