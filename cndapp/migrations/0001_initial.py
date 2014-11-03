# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuvant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Anaesthesia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('requires_comment', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['sort', 'name'],
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
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(default=10)),
                ('requires_comment', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['group__sort', 'sort', 'name'],
                'verbose_name_plural': 'diagnoses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiagnosisGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DOBPrecision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('css_class', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EthnicGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('requires_comment', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['group', 'sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EthnicGroupGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['sort', 'name'],
                'verbose_name': 'Ethnic group / Race',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eye',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('single', models.BooleanField()),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HealthCare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IOPAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('no_agents', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LensStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['group__sort', 'sort', 'name'],
                'verbose_name_plural': 'lens statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LensStatusGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('comments', models.TextField(blank=True)),
                ('adjuvant', models.ForeignKey(blank=True, to='cndapp.Adjuvant', null=True)),
                ('agents', models.ManyToManyField(to='cndapp.IOPAgent', verbose_name=b'IOP Agents', blank=True)),
                ('complication', models.ForeignKey(blank=True, to='cndapp.Complication', null=True)),
                ('created_by', models.ForeignKey(related_name='management_created_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('eye', models.ForeignKey(blank=True, to='cndapp.Eye', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ManagementType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('iop_control_right', models.IntegerField(verbose_name=b'Right IOP Control', choices=[(1, b'Controlled'), (2, b'Uncontrolled'), (3, b'Not applicable')])),
                ('iop_control_left', models.IntegerField(verbose_name=b'Left IOP Control', choices=[(1, b'Controlled'), (2, b'Uncontrolled'), (3, b'Not applicable')])),
                ('iop_right', models.IntegerField(verbose_name=b'Right IOP', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('iop_left', models.IntegerField(verbose_name=b'Left IOP', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('visual_acuity_method_comment', models.TextField(verbose_name=b'Method Comment', blank=True)),
                ('visual_acuity_fixation_preference', models.IntegerField(blank=True, null=True, verbose_name=b'Fixation Preference', choices=[(2, b'Right'), (3, b'Left'), (1, b'None')])),
                ('created_by', models.ForeignKey(related_name='outcome_created_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('eua', models.ForeignKey(verbose_name=b'EUA', to='cndapp.Anaesthesia')),
                ('iop_agents_left', models.ManyToManyField(related_name='outcome_iop_agents_left', verbose_name=b'IOP Agents Left', to='cndapp.IOPAgent')),
                ('iop_agents_right', models.ManyToManyField(related_name='outcome_iop_agents_right', verbose_name=b'IOP Agents Right', to='cndapp.IOPAgent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(default=uuid.uuid4, unique=True, max_length=64, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('next_reminder', models.DateField(auto_now_add=True, null=True)),
                ('outcome_overdue', models.BooleanField(default=False)),
                ('sex', models.IntegerField(choices=[(0, b'Male'), (1, b'Female')])),
                ('dob_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('dob_month', models.IntegerField(blank=True, null=True, choices=[(1, b'01'), (2, b'02'), (3, b'03'), (4, b'04'), (5, b'05'), (6, b'06'), (7, b'07'), (8, b'08'), (9, b'09'), (10, b'10'), (11, b'11'), (12, b'12')])),
                ('dob_year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2014), django.core.validators.MinValueValidator(1984)])),
                ('postcode', models.CharField(max_length=6, verbose_name=b'Post/Zip Code')),
                ('ethnic_group_comment', models.CharField(max_length=255, blank=True)),
                ('consanguinity', models.IntegerField(choices=[(2, b'Unknown'), (0, b'No'), (1, b'Yes')])),
                ('history', models.IntegerField(verbose_name=b'Family History of Childhood Onset Glaucoma', choices=[(2, b'Unknown'), (0, b'No'), (1, b'Yes')])),
                ('history_comment', models.TextField(blank=True)),
                ('diagnosis_right_comment', models.TextField(verbose_name=b'Right Diagnosis comment', blank=True)),
                ('diagnosis_left_comment', models.TextField(verbose_name=b'Left Diagnosis comment', blank=True)),
                ('lens_extraction_date_right', models.DateField(null=True, verbose_name=b'Right Extraction Date', blank=True)),
                ('lens_extraction_date_left', models.DateField(null=True, verbose_name=b'Left Extraction Date', blank=True)),
                ('visual_acuity_date', models.DateField(verbose_name=b'Date')),
                ('visual_acuity_method_comment', models.TextField(verbose_name=b'Method Comment', blank=True)),
                ('visual_acuity_fixation_preference', models.IntegerField(blank=True, null=True, verbose_name=b'Fixation Preference', choices=[(2, b'Right'), (3, b'Left'), (1, b'None')])),
                ('iop_right', models.IntegerField(verbose_name=b'Right IOP', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('iop_left', models.IntegerField(verbose_name=b'Left IOP', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('comments', models.TextField(blank=True)),
                ('country', models.ForeignKey(verbose_name=b'Country of Residence', to='cndapp.Country')),
                ('created_by', models.ForeignKey(related_name='patient_created_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('diagnosis_left', models.ForeignKey(related_name='+', verbose_name=b'Left Diagnosis', to='cndapp.Diagnosis')),
                ('diagnosis_right', models.ForeignKey(related_name='+', verbose_name=b'Right Diagnosis', to='cndapp.Diagnosis')),
                ('ethnic_group', models.ForeignKey(verbose_name=b'Ethnic Group / Race', to='cndapp.EthnicGroup')),
                ('eua', models.ForeignKey(verbose_name=b'EUA', to='cndapp.Anaesthesia')),
                ('health_care', models.ForeignKey(verbose_name=b'Health Care Coverage', to='cndapp.HealthCare')),
                ('iop_agents_left', models.ManyToManyField(related_name='patient_iop_agents_left', verbose_name=b'Left IOP Agents', to='cndapp.IOPAgent')),
                ('iop_agents_right', models.ManyToManyField(related_name='patient_iop_agents_right', verbose_name=b'Right IOP Agents', to='cndapp.IOPAgent')),
                ('lens_status_left', models.ForeignKey(related_name='+', verbose_name=b'Left Lens Status', to='cndapp.LensStatus')),
                ('lens_status_right', models.ForeignKey(related_name='+', verbose_name=b'Right Lens Status', to='cndapp.LensStatus')),
            ],
            options={
                'ordering': ['-updated_at'],
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
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('adjuvant', models.BooleanField()),
                ('stage', models.BooleanField()),
                ('sort', models.IntegerField(default=10)),
                ('requires_comment', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['sort', 'name'],
                'verbose_name_plural': 'Surgeries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurgeryStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tonometry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob_min_precision', models.ForeignKey(related_name='+', default=1, verbose_name=b'DOB Minimum Precision', to='cndapp.DOBPrecision')),
                ('dob_precision', models.ForeignKey(related_name='+', default=1, verbose_name=b'DOB Maximum Precision', to='cndapp.DOBPrecision')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityCorrection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('beo', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
                ('not_recorded', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['scale__name', 'sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualAcuityScale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('sort', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['sort', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='visualacuityreading',
            name='scale',
            field=models.ForeignKey(related_name='readings', to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visualacuitymethod',
            name='scales',
            field=models.ManyToManyField(to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='tonometry',
            field=models.ForeignKey(to='cndapp.Tonometry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_by',
            field=models.ForeignKey(related_name='patient_updated_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_both',
            field=models.ForeignKey(related_name='patient_beo', verbose_name=b'Both Eyes Open', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_correction_both',
            field=models.ForeignKey(related_name='patient_beo_correction', verbose_name=b'Both correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_correction_left',
            field=models.ForeignKey(related_name='patient_lva_correction', verbose_name=b'Left correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_correction_right',
            field=models.ForeignKey(related_name='patient_rva_correction', verbose_name=b'Right correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_left',
            field=models.ForeignKey(related_name='patient_lva', verbose_name=b'LVA', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_method',
            field=models.ForeignKey(verbose_name=b'Method', to='cndapp.VisualAcuityMethod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_right',
            field=models.ForeignKey(related_name='patient_rva', verbose_name=b'RVA', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='visual_acuity_scale',
            field=models.ForeignKey(related_name='patient_visualacuity_scale', verbose_name=b'Scale', to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='patient',
            field=models.ForeignKey(to='cndapp.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='tonometry',
            field=models.ForeignKey(to='cndapp.Tonometry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='updated_by',
            field=models.ForeignKey(related_name='outcome_updated_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_both',
            field=models.ForeignKey(related_name='outcome_beo', verbose_name=b'Both Eyes Open', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_correction_both',
            field=models.ForeignKey(related_name='outcome_beo_correction', verbose_name=b'Both correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_correction_left',
            field=models.ForeignKey(related_name='outcome_lva_correction', verbose_name=b'Left correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_correction_right',
            field=models.ForeignKey(related_name='outcome_rva_correction', verbose_name=b'Right correction', blank=True, to='cndapp.VisualAcuityCorrection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_left',
            field=models.ForeignKey(related_name='outcome_lva', verbose_name=b'LVA', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_method',
            field=models.ForeignKey(to='cndapp.VisualAcuityMethod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_right',
            field=models.ForeignKey(related_name='outcome_rva', verbose_name=b'RVA', to='cndapp.VisualAcuityReading'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='outcome',
            name='visual_acuity_scale',
            field=models.ForeignKey(related_name='outcome_visualacuity_scale', verbose_name=b'Scale', to='cndapp.VisualAcuityScale'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='management',
            name='patient',
            field=models.ForeignKey(to='cndapp.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='management',
            name='surgery',
            field=models.ForeignKey(blank=True, to='cndapp.Surgery', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='management',
            name='surgery_stage',
            field=models.ForeignKey(blank=True, to='cndapp.SurgeryStage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='management',
            name='type',
            field=models.ForeignKey(to='cndapp.ManagementType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='management',
            name='updated_by',
            field=models.ForeignKey(related_name='management_updated_set', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lensstatus',
            name='group',
            field=models.ForeignKey(to='cndapp.LensStatusGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ethnicgroup',
            name='group',
            field=models.ForeignKey(to='cndapp.EthnicGroupGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='group',
            field=models.ForeignKey(to='cndapp.DiagnosisGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='postcode_validator',
            field=models.ForeignKey(to='cndapp.PostcodeValidator'),
            preserve_default=True,
        ),
    ]
