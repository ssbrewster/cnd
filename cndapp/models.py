from django.contrib.auth.models import User
from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models
from django import forms
from uuidfield import UUIDField
import datetime


class PostcodeValidator(models.Model):
    pattern = models.CharField(max_length=64)
    error = models.CharField(max_length=255)

    def __unicode__(self):
        return self.pattern


class Country(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField(default=10)
    iso = models.CharField(max_length=2)
    postcode_validator = models.ForeignKey(PostcodeValidator)

    class Meta:
        ordering = ['sort', 'name']

    def __unicode__(self):
        return self.name

# Lookup tables


class AdditionalProcedure(models.Model):
    name = models.CharField(max_length=85)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class AnaestheticType(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class Complication(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class DifficultyFactor(models.Model):
    name = models.CharField(max_length=85)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class Eye(models.Model):
    name = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name


class IolPosition(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class KeratomyUnit(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class OcularCopathology(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class PostOpComplication(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class RefractionType(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class SurgeonGrade(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class SurgeryReason(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class VisualAcuityCorrection(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name


class VisualAcuityScale(models.Model):
    name = models.CharField(max_length=64)
    sort = models.IntegerField()

    class Meta:
        ordering = ['sort']

    def __unicode__(self):
        return self.name

# Form data


class Patient(models.Model):
    uuid = UUIDField(auto=True, unique=True)
    created_by = models.ForeignKey(User, related_name='patient_created_set', blank=True, null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='patient_updated_set', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.ForeignKey(Gender)
    postcode = models.CharField(max_length=4)  # TODO validation
    treated_eye = models.ForeignKey(Eye)

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)


class EyedrawField(models.TextField):

    def __init__(self, *args, **kwargs):
        super(EyedrawField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': forms.HiddenInput}
        defaults.update(kwargs)
        return super(EyedrawField, self).formfield(**defaults)


class PreOpAssessment(models.Model):
    patient = models.ForeignKey(Patient, unique=True)

    date = models.DateField(default=datetime.date.today)

    morphology = EyedrawField()
    STATE_CHOICES = (
        (True, u'Yes'),
        (False, u'No'),
    )
    diabetes = models.BooleanField(default=None, choices=STATE_CHOICES)
    alpha_blockers = models.BooleanField(default=None, choices=STATE_CHOICES)
    able_to_cooperate = models.BooleanField(default=None, choices=STATE_CHOICES)
    able_to_lie_flat = models.BooleanField(default=None, choices=STATE_CHOICES)
    ocular_copathology = models.ManyToManyField(OcularCopathology)
    guarded_prognosis = models.BooleanField(default=None, choices=STATE_CHOICES)

    # Biometry
    keratomy_unit = models.ForeignKey(KeratomyUnit, verbose_name='Keratometry unit')
    k1 = models.DecimalField(max_digits=4, decimal_places=2)
    k2 = models.DecimalField(max_digits=4, decimal_places=2)
    axis_k1 = models.DecimalField(max_digits=4, decimal_places=1, validators=[validators.MinValueValidator(0.5), validators.MaxValueValidator(180)])
    axial_length = models.DecimalField(max_digits=4, decimal_places=2)
    desired_refraction = models.DecimalField(max_digits=4, decimal_places=2)
    predicted_refraction = models.DecimalField(max_digits=4, decimal_places=2)
    iol_power = models.DecimalField(verbose_name='IOL power', max_digits=4, decimal_places=2)

    def __unicode__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.patient.id})

    def left_va_readings(self):
        return self.preopassessmentvisualacuityreading_set.filter(eye__name="Left")

    def right_va_readings(self):
        return self.preopassessmentvisualacuityreading_set.filter(eye__name="Right")


class PreOpAssessmentVisualAcuityReading(models.Model):
    preopassessment = models.ForeignKey(PreOpAssessment)
    eye = models.ForeignKey(Eye)
    scale = models.ForeignKey(VisualAcuityScale)
    correction = models.ForeignKey(VisualAcuityCorrection)
    value = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return str(self.pk)


class OpNote(models.Model):
    patient = models.ForeignKey(Patient, unique=True)

    date = models.DateField(default=datetime.date.today)
    age = models.PositiveIntegerField()

    anaesthetic = models.ManyToManyField(AnaestheticType)
    surgeon_grade = models.ForeignKey(SurgeonGrade)
    STATE_CHOICES = (
        (True, u'Yes'),
        (False, u'No'),
    )
    first_eye = models.BooleanField(default=None, choices=STATE_CHOICES)
    primary_reason = models.ForeignKey(SurgeryReason)
    lens_inserted = models.BooleanField(default=None, choices=STATE_CHOICES)

    eyedraw = EyedrawField()

    difficulty_factors = models.ManyToManyField(DifficultyFactor)
    iol_position = models.ForeignKey(IolPosition)
    additional_procedures = models.ManyToManyField(AdditionalProcedure)
    complications = models.ManyToManyField(Complication)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.patient.id})


class FollowUp(models.Model):
    patient = models.ForeignKey(Patient, unique=True)
    date = models.DateField(default=datetime.date.today)
    complications = models.ManyToManyField(PostOpComplication)

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.patient.id})

    def left_va_readings(self):
        return self.followupvisualacuityreading_set.filter(eye__name="Left")

    def right_va_readings(self):
        return self.followupvisualacuityreading_set.filter(eye__name="Right")

    def left_refraction(self):
        return self.followuprefraction_set.get(eye__name="Left")

    def right_refraction(self):
        return self.followuprefraction_set.get(eye__name="Right")


class FollowUpVisualAcuityReading(models.Model):
    followup = models.ForeignKey(FollowUp)
    eye = models.ForeignKey(Eye)
    scale = models.ForeignKey(VisualAcuityScale)
    correction = models.ForeignKey(VisualAcuityCorrection)
    value = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return str(self.pk)


class FollowUpRefraction(models.Model):
    followup = models.ForeignKey(FollowUp)
    eye = models.ForeignKey(Eye)
    eyedraw = EyedrawField()
    type = models.ForeignKey(RefractionType)
    sphere = models.DecimalField(max_digits=4, decimal_places=2)
    cylinder = models.DecimalField(max_digits=4, decimal_places=2)
    axis = models.DecimalField(max_digits=4, decimal_places=1, default=0, validators=[validators.MinValueValidator(0.5), validators.MaxValueValidator(180)])

    class Meta:
        unique_together = ("followup", "eye")
