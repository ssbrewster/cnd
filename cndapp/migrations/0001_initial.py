# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.db.models.deletion
from django.conf import settings
import uuidfield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProcedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnaestheticType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
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
            name='DifficultyFactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eye',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('left_refraction', jsonfield.fields.JSONField()),
                ('right_refraction', jsonfield.fields.JSONField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FollowUpVisualAcuityReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IolPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeratomyUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OcularCopathology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('age', models.IntegerField()),
                ('first_eye', models.BooleanField()),
                ('lens_inserted', models.BooleanField()),
                ('eyedraw', jsonfield.fields.JSONField()),
                ('additional_procedures', models.ManyToManyField(to='cndapp.AdditionalProcedure')),
                ('anaesthetic', models.ManyToManyField(to='cndapp.AnaestheticType')),
                ('complications', models.ManyToManyField(to='cndapp.Complication')),
                ('difficulty_factors', models.ManyToManyField(to='cndapp.DifficultyFactor')),
                ('iol_position', models.ForeignKey(to='cndapp.IolPosition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('postcode', models.CharField(max_length=4)),
                ('created_by', models.ForeignKey(related_name='patient_created_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('gender', models.ForeignKey(to='cndapp.Gender')),
                ('treated_eye', models.ForeignKey(to='cndapp.Eye')),
                ('updated_by', models.ForeignKey(related_name='patient_updated_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
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
        migrations.CreateModel(
            name='PostOpComplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreOpAssessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('morphology', jsonfield.fields.JSONField()),
                ('diabetes', models.BooleanField()),
                ('alpha_blockers', models.BooleanField()),
                ('able_to_cooperate', models.BooleanField()),
                ('able_to_lie_flat', models.BooleanField()),
                ('guarded_prognosis', models.BooleanField()),
                ('k1', models.DecimalField(max_digits=4, decimal_places=2)),
                ('k2', models.DecimalField(max_digits=4, decimal_places=2)),
                ('axis_k1', models.DecimalField(max_digits=4, decimal_places=1, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(180)])),
                ('axial_length', models.DecimalField(max_digits=4, decimal_places=2)),
                ('desired_refraction', models.DecimalField(max_digits=4, decimal_places=2)),
                ('predicted_refraction', models.DecimalField(max_digits=4, decimal_places=2)),
                ('iol_power', models.DecimalField(max_digits=4, decimal_places=2)),
                ('keratomy_unit', models.ForeignKey(to='cndapp.KeratomyUnit')),
                ('ocular_copathology', models.ManyToManyField(to='cndapp.OcularCopathology')),
                ('patient', models.ForeignKey(to='cndapp.Patient', unique=True)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurgeonGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurgeryReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityCorrection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityScale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField()),
            ],
            options={
                'ordering': ['sort'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='preopassessmentvisualacuityreading',
            name='correction',
            field=models.ForeignKey(to='cndapp.VisualAcuityCorrection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='preopassessmentvisualacuityreading',
            name='eye',
            field=models.ForeignKey(to='cndapp.Eye'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='preopassessmentvisualacuityreading',
            name='preopassessment',
            field=models.ForeignKey(to='cndapp.PreOpAssessment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='preopassessmentvisualacuityreading',
            name='scale',
            field=models.ForeignKey(to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opnote',
            name='patient',
            field=models.ForeignKey(to='cndapp.Patient', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opnote',
            name='primary_reason',
            field=models.ForeignKey(to='cndapp.SurgeryReason'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opnote',
            name='surgeon_grade',
            field=models.ForeignKey(to='cndapp.SurgeonGrade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followupvisualacuityreading',
            name='correction',
            field=models.ForeignKey(to='cndapp.VisualAcuityCorrection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followupvisualacuityreading',
            name='eye',
            field=models.ForeignKey(to='cndapp.Eye'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followupvisualacuityreading',
            name='followup',
            field=models.ForeignKey(to='cndapp.FollowUp'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followupvisualacuityreading',
            name='scale',
            field=models.ForeignKey(to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followup',
            name='complications',
            field=models.ManyToManyField(to='cndapp.PostOpComplication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followup',
            name='patient',
            field=models.ForeignKey(to='cndapp.Patient', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='postcode_validator',
            field=models.ForeignKey(to='cndapp.PostcodeValidator'),
            preserve_default=True,
        ),
    ]
