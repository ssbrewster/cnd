
from django.views.generic import TemplateView,  CreateView, FormView
from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from cndapp.forms import *
from .models import  Patient, PreOpAssessment, OpNote, FollowUp,  Eye
from .serializers import PatientSerializer, PreOpAssessmentSerializer, OpNoteSerializer, FollowUpSerializer



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


class FollowUpViewSet(viewsets.ModelViewSet):
    """
    This endpoint represents the follow-ups in the database.
    """
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer


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