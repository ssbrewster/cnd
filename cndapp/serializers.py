from django.forms import widgets
from rest_framework import serializers
from .models import Patient, Gender


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.RelatedField(read_only=False)
    treated_eye = serializers.RelatedField(read_only=False)

    class Meta:
        model = Patient
        fields = ('url', 'uuid', 'gender', 'postcode', 'treated_eye')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    patients = serializers.HyperlinkedRelatedField(view_name='patient-list')

    class Meta:
        model = Gender
        fields = ('url', 'gender', 'patients')