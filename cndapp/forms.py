from django import forms
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from captcha.fields import ReCaptchaField
from cndapp.models import PreOpAssessment, PreOpAssessmentVisualAcuityReading, FollowUp, FollowUpVisualAcuityReading, FollowUpRefraction, OpNote
import datetime

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        message = get_template('cndapp/message.txt')
        d = Context(self.cleaned_data)
        send_mail('Message from CND contact form', message.render(d), settings.CONTACT_SENDER, settings.CONTACT_RECIPIENTS)

class CaptchaContactForm(ContactForm):
    captcha = ReCaptchaField()

class PreOpAssessmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PreOpAssessmentForm, self).__init__(*args, **kwargs)
        self.fields['diabetes'].required = True
        self.fields['alpha_blockers'].required = True
        self.fields['able_to_cooperate'].required = True
        self.fields['able_to_lie_flat'].required = True
        self.fields['guarded_prognosis'].required = True

    class Meta:
        model = PreOpAssessment
        fields = ('date', 'morphology', 'diabetes', 'alpha_blockers', 'able_to_cooperate', 'able_to_lie_flat',
                  'ocular_copathology', 'guarded_prognosis', 'keratomy_unit', 'k1', 'k2', 'axis_k1', 'axial_length',
                  'desired_refraction', 'predicted_refraction', 'iol_power')
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker past'}),
            'diabetes': forms.RadioSelect(),
            'alpha_blockers': forms.RadioSelect(),
            'able_to_cooperate': forms.RadioSelect(),
            'able_to_lie_flat': forms.RadioSelect(),
            'guarded_prognosis': forms.RadioSelect(),
            'morphology': forms.HiddenInput(),
        }
    morphology_tools = [
        {'name': 'PI', 'label': 'Peripheral Iridectomy'},
        {'name': 'NuclearCataract', 'label': 'Nuclear Cataract'},
        {'name': 'CorticalCataract', 'label': 'Cortical Cataract'},
        {'name': 'PostSubcapCataract', 'label': 'Posterior Subcapsular Cataract'},
    ]

PreOpAssessmentVisualAcuityReadingFormSet = \
    forms.models.inlineformset_factory(PreOpAssessment, PreOpAssessmentVisualAcuityReading, extra = 1, can_delete = False)

class OpNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OpNoteForm, self).__init__(*args, **kwargs)
        self.fields['first_eye'].required = True
        self.fields['lens_inserted'].required = True

    class Meta:
        model = OpNote
        fields = ('date', 'age', 'anaesthetic', 'surgeon_grade', 'first_eye', 'primary_reason', 'lens_inserted',
                  'eyedraw', 'difficulty_factors', 'iol_position', 'additional_procedures', 'complications')
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker past'}),
            'first_eye': forms.RadioSelect(),
            'lens_inserted': forms.RadioSelect(),
        }
    eyedraw_tools = [
        {'name': 'PhakoIncision', 'label': 'Phako Incision'},
        {'name': 'SidePort', 'label': 'Side Port'},
        {'name': 'IrisHook', 'label': 'Iris Hook'},
        {'name': 'PCIOL', 'label': 'PCIOL'},
        {'name': 'ACIOL', 'label': 'ACIOL'},
        {'name': 'PI', 'label': 'PI'},
        {'name': 'MattressSuture', 'label': 'Mattress Suture'},
        {'name': 'CapsularTensionRing', 'label': 'Capsular Tension Ring'},
        {'name': 'CornealSuture', 'label': 'Corneal Suture'},
        {'name': 'ToricPCIOL', 'label': 'Toric PCIOL'},
        {'name': 'LimbalRelaxingIncision', 'label': 'Limbal Relaxing Incision'}
    ]

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        exclude = ( 'patient', 'created_by', 'updated_by', )
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker past'}),
        }

FollowUpVisualAcuityReadingFormSet = \
    forms.models.inlineformset_factory(FollowUp, FollowUpVisualAcuityReading, extra = 1, can_delete = False)

class FollowUpRefractionForm(forms.ModelForm):
    class Meta:
        model = FollowUpRefraction
        exclude = ( 'followup', )
        widgets = {
            'eye': forms.HiddenInput(),
        }
