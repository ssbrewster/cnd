from django.forms import widgets
from rest_framework import serializers
from .models import Patient, PreOpAssessment, OpNote, Gender


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.RelatedField()
    treated_eye = serializers.RelatedField(read_only=False)

    class Meta:
        model = Patient
        fields = ('url', 'uuid', 'gender', 'postcode', 'treated_eye')


class PreOpAssessmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail')

    class Meta:
        model = PreOpAssessment
        fields = ('url', 'patient')


class OpNoteSerializer(serializers.HyperlinkedRelatedField):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail')
    surgeon_grade = serializers.RelatedField()
    primary_reason = serializers.RelatedField()
    iol_position = serializers.RelatedField()

    class Meta:
        model = OpNote
        fields = ('url', 'date', 'age', 'anaesthetic', 'surgeon_grade', 'first_eye', 'primary_reason', 'lens_inserted',
                    'eyedraw', 'difficulty_factors', 'iol_position', 'additional_procedures', 'complications')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    patients = serializers.HyperlinkedRelatedField(view_name='patient-list')

    class Meta:
        model = Gender
        fields = ('url', 'gender', 'patients')