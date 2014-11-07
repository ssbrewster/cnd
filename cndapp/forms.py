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
    class Meta:
        model = PreOpAssessment
        exclude = ( 'patient', 'created_by', 'updated_by', )
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
    class Meta:
        model = OpNote
        exclude = ( 'patient', 'created_by', 'updated_by' )
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
