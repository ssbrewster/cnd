
from django.views.generic import TemplateView,  CreateView, FormView
from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from cndapp.forms import *
from .models import  Patient, PreOpAssessment, OpNote, FollowUp,  Eye
from .serializers import PatientSerializer, PreOpAssessmentSerializer, OpNoteSerializer



class IndexView(TemplateView):
    template_name = 'cndapp/index.html'


class AboutView(TemplateView):
    template_name = 'cndapp/about.html'


class HelpView(TemplateView):
    template_name = 'cndapp/help.html'


class ContactView(FormView):
    template_name = 'cndapp/contact.html'
    success_url = '/cndapp/thanks/'

    def get_form_class(self):
        if self.request.user.is_authenticated():
            return ContactForm
        else:
            return CaptchaContactForm
    
    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'cndapp/thanks.html'


class PatientViewSet(viewsets.ModelViewSet):
    """
    This endpoint represents the patients that have been added to the database.

    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PreOpAssessmentViewSet(viewsets.ModelViewSet):
    """
    This endpoint represents the pre-op assessments in the database.
    """
    queryset = PreOpAssessment.objects.all()
    serializer_class = PreOpAssessmentSerializer


class OpNoteViewSet(viewsets.ModelViewSet):
    """
    This endpoint represents the op-notes in the database.
    """
    queryset = OpNote.objects.all()
    serializer_class = OpNoteSerializer


class FollowUpCreateView(CreateView):
    model = FollowUp
    form_class = FollowUpForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.patient = get_object_or_404(Patient, pk=self.kwargs['patient'])
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        va_form = FollowUpVisualAcuityReadingFormSet()
        refr_form_r = FollowUpRefractionForm(initial = {'eye': Eye.objects.get(name = 'Right')}, prefix = 'r')
        refr_form_l = FollowUpRefractionForm(initial = {'eye': Eye.objects.get(name = 'Left')}, prefix = 'l')
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form, va_form=va_form, refr_form_r = refr_form_r, refr_form_l = refr_form_l))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.patient = get_object_or_404(Patient, pk=self.kwargs['patient'])
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        va_form = FollowUpVisualAcuityReadingFormSet(self.request.POST)
        refr_form_r = FollowUpRefractionForm(self.request.POST, initial = {'eye': Eye.objects.get(name = 'Right')}, prefix = 'r')
        refr_form_l = FollowUpRefractionForm(self.request.POST, initial = {'eye': Eye.objects.get(name = 'Left')}, prefix = 'l')

        if (form.is_valid() and va_form.is_valid() and refr_form_r.is_valid() and refr_form_l.is_valid()):
            return self.form_valid(form, va_form, [refr_form_r, refr_form_l])
        else:
            return self.form_invalid(form, va_form, refr_form_r, refr_form_l)

    def form_valid(self, form, va_form, refr_forms):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.patient = self.patient
        self.object = form.save()
        va_form.instance = self.object
        va_form.save()
        for refr_form in refr_forms:
            refr_form.instance.followup = self.object
            refr_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, va_form, refr_form_r, refr_form_l):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        print refr_form_r.errors
        print refr_form_l.errors
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form, va_form=va_form, refr_form_r = refr_form_r, refr_form_l = refr_form_l))


class PatientByGenderList(generics.ListAPIView):
    """
    This endpoint lists all patients by gender
    """
    serializer_class = PatientSerializer

    def get_queryset(self):
        """
        :return: queryset of patients restricted by gender.
        """
        queryset = Patient.objects.all()
        gender = self.request.QUERY_PARAMS.get('gender', None)
        if gender is not None:
            queryset = queryset.filter(gender__name=gender)
        return queryset