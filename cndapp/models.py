from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from uuid import uuid4
from datetime import date

from django.core.urlresolvers import reverse

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

class Patient(models.Model):
    uuid = models.CharField(unique=True, max_length=64, editable=False, blank=True, default=uuid4)
    created_by = models.ForeignKey(User, related_name='patient_created_set', blank=True, null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='patient_updated_set', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    MALE = 0
    FEMALE = 1
    SEX_CHOICES = (
                   (MALE, 'Male'),
                   (FEMALE, 'Female'),
    )
    sex = models.IntegerField(choices=SEX_CHOICES)
    dob_year = models.IntegerField(validators=[
                                               validators.MaxValueValidator(date.today().year),
                                               validators.MinValueValidator(date.today().year - 30)
                                               ])

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.uuid

class First(models.Model):
    name = models.CharField(max_length=64)
    patient = models.ForeignKey(Patient)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.name

class Second(models.Model):
    name = models.CharField(max_length=64)
    patient = models.ForeignKey(Patient)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.name

class Third(models.Model):
    name = models.CharField(max_length=64)
    patient = models.ForeignKey(Patient)

    def get_absolute_url(self):
        return reverse('list')

    def __unicode__(self):
        return self.name

