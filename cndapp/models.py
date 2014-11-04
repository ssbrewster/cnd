from django.contrib.auth.models import User
from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models
from jsonfield import JSONField
from uuidfield import UUIDField

class PostcodeValidator(models.Model):
    pattern = models.CharField(max_length=64)
    error = models.CharField(max_length=255)

    def __unicode__(self):
        return self.pattern

class Country(models.Model):
    class Meta:
        ordering = ['sort', 'name']

    name = models.CharField(max_length=64)
    sort = models.IntegerField(default=10)
    iso = models.CharField(max_length=2)
    postcode_validator = models.ForeignKey(PostcodeValidator)

    def __unicode__(self):
        return self.name

# Lookup tables

class AdditionalProcedure(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 85)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class AnaestheticType(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class Complication(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class DifficultyFactor(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 85)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class Eye(models.Model):
    name = models.CharField(max_length = 5)

    def __unicode__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length = 12)

    def __unicode__(self):
        return self.name

class IolPosition(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class KeratomyUnit(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class OcularCopathology(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class PostOpComplication(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class SurgeonGrade(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class SurgeryReason(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class VisualAcuityCorrection(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

class VisualAcuityScale(models.Model):
    class Meta:
        ordering = ['sort']

    name = models.CharField(max_length = 64)
    sort = models.IntegerField()

    def __unicode__(self):
        return self.name

# Form data

class Patient(models.Model):
    uuid = UUIDField(auto = True, unique = True)
    created_by = models.ForeignKey(User, related_name='patient_created_set', blank=True, null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='patient_updated_set', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.ForeignKey(Gender)
    postcode = models.CharField(max_length = 4)  # TODO validation
    treated_eye = models.ForeignKey(Eye)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.uuid.hex

class PreOpAssessment(models.Model):
    patient = models.ForeignKey(Patient, unique = True)

    date = models.DateField()

    morphology = JSONField()
    diabetes = models.BooleanField()
    alpha_blockers = models.BooleanField()
    able_to_cooperate = models.BooleanField()
    able_to_lie_flat = models.BooleanField()
    ocular_copathology = models.ManyToManyField(OcularCopathology)
    guarded_prognosis = models.BooleanField()

    # Biometry
    keratomy_unit = models.ForeignKey(KeratomyUnit)
    k1 = models.DecimalField(max_digits = 4, decimal_places = 2)
    k2 = models.DecimalField(max_digits = 4, decimal_places = 2)
    axis_k1 = models.DecimalField(max_digits = 4, decimal_places = 1, validators = [validators.MinValueValidator(0.5), validators.MaxValueValidator(180)])
    axial_length = models.DecimalField(max_digits = 4, decimal_places = 2)
    desired_refraction = models.DecimalField(max_digits = 4, decimal_places = 2)
    predicted_refraction = models.DecimalField(max_digits = 4, decimal_places = 2)
    iol_power = models.DecimalField(max_digits = 4, decimal_places = 2)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.pk

class PreOpAssessmentVisualAcuityReading(models.Model):
    preopassessment = models.ForeignKey(PreOpAssessment)
    eye = models.ForeignKey(Eye)
    scale = models.ForeignKey(VisualAcuityScale)
    correction = models.ForeignKey(VisualAcuityCorrection)
    value = models.DecimalField(max_digits = 3, decimal_places = 2)

    def __unicode__(self):
        return self.value

class OpNote(models.Model):
    patient = models.ForeignKey(Patient, unique = True)

    date = models.DateField()
    age = models.IntegerField()

    anaesthetic = models.ManyToManyField(AnaestheticType)
    surgeon_grade = models.ForeignKey(SurgeonGrade)
    first_eye = models.BooleanField()
    primary_reason = models.ForeignKey(SurgeryReason)
    lens_inserted = models.BooleanField()

    # The cut-down dataset doesn't require this but Bill thinks we should include it because it looks cool
    eyedraw = JSONField()

    difficulty_factors = models.ManyToManyField(DifficultyFactor)
    iol_position = models.ForeignKey(IolPosition)
    additional_procedures = models.ManyToManyField(AdditionalProcedure)
    complications = models.ManyToManyField(Complication)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.pk

class FollowUp(models.Model):
    patient = models.ForeignKey(Patient, unique = True)

    date = models.DateField()

    left_refraction = JSONField()
    right_refraction = JSONField()
    complications = models.ManyToManyField(PostOpComplication)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.pk

class FollowUpVisualAcuityReading(models.Model):
    followup = models.ForeignKey(FollowUp)
    eye = models.ForeignKey(Eye)
    scale = models.ForeignKey(VisualAcuityScale)
    correction = models.ForeignKey(VisualAcuityCorrection)
    value = models.DecimalField(max_digits = 3, decimal_places = 2)

    def __unicode__(self):
        return self.value

