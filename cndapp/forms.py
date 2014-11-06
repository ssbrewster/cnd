from django import forms
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from captcha.fields import ReCaptchaField
from cndapp.models import PreOpAssessment, PreOpAssessmentVisualAcuityReading, FollowUp, FollowUpVisualAcuityReading, OpNote


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
        exclude = ( 'patient', 'created_by', 'updated_by', )
        widgets = {
            'first_eye': forms.RadioSelect(),
            'lens_inserted': forms.RadioSelect(),
        }

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        exclude = ( 'patient', 'created_by', 'updated_by', )

FollowUpVisualAcuityReadingFormSet = \
    forms.models.inlineformset_factory(FollowUp, FollowUpVisualAcuityReading, extra = 1, can_delete = False)
