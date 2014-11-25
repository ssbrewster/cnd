from django.forms import widgets
from rest_framework import serializers
from .models import Patient, PreOpAssessment, OpNote, Gender, Eye


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.SlugRelatedField(read_only=False, slug_field='name')
    treated_eye = serializers.SlugRelatedField(read_only=False, slug_field='name')

    class Meta:
        model = Patient
        fields = ('url', 'uuid', 'gender', 'postcode', 'treated_eye')


class PreOpAssessmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail')
    ocular_copathology = serializers.SlugRelatedField(read_only=False, many=True, slug_field='name')
    keratomy_unit = serializers.SlugRelatedField(read_only=False, slug_field='name')

    class Meta:
        model = PreOpAssessment
        fields = ('url', 'patient', 'date', #'morphology',
         'diabetes', 'alpha_blockers', 'able_to_cooperate',
        'able_to_lie_flat', 'ocular_copathology', 'guarded_prognosis', 'keratomy_unit', 'k1', 'k2', 'axis_k1',
         'axial_length', 'desired_refraction', 'predicted_refraction', 'iol_power')


class OpNoteSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient-detail')
    anaesthetic = serializers.SlugRelatedField(read_only=False, many=True, slug_field='name')
    surgeon_grade = serializers.SlugRelatedField(read_only=False, slug_field='name')
    primary_reason = serializers.SlugRelatedField(read_only=False, slug_field='name')
    difficulty_factors = serializers.SlugRelatedField(read_only=False, many=True, slug_field='name')
    iol_position = serializers.SlugRelatedField(read_only=False, slug_field='name')
    additional_procedures = serializers.SlugRelatedField(read_only=False, many=True, slug_field='name')
    complications = serializers.SlugRelatedField(read_only=False, many=True, slug_field='name')

    class Meta:
        model = OpNote
        fields = ('url', 'patient', 'date', 'age', 'anaesthetic', 'surgeon_grade', 'first_eye', 'primary_reason', 'lens_inserted',
                    #'eyedraw',
                    'difficulty_factors', 'iol_position', 'additional_procedures', 'complications')


class GenderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gender
        fields = ('url', 'name')