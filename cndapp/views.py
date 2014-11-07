from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, DeleteView, RedirectView
from django.utils.decorators import method_decorator
from django.contrib.sites.models import get_current_site
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from cndapp.forms import *
from cndapp.models import Eye, Patient, PreOpAssessment, OpNote, FollowUp

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

class PatientListView(ListView):
     context_object_name = 'patients'

     def get_queryset(self):
          return Patient.objects.filter(created_by=self.request.user)

     @method_decorator(login_required)
     def dispatch(self, request, *args, **kwargs):
         return super(PatientListView, self).dispatch(request, *args, **kwargs)

class PatientDetailView(DetailView):
    context_object_name = 'patient'

    def get_queryset(self):
          return Patient.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['patient_url'] = 'http://' + get_current_site(self.request).domain + '/cndapp/uuid/' + str(self.get_object().uuid)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientDetailView, self).dispatch(request, *args, **kwargs)

class PatientUUIDView(RedirectView):
    def get_redirect_url(self, **kwargs):
        try:
            patient = Patient.objects.get(uuid=kwargs['uuid'])
            return '/cndapp/detail/' + str(patient.pk)
        except:
            raise Http404

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientUUIDView, self).dispatch(request, *args, **kwargs)

class PatientCreateView(CreateView):
    model = Patient
    fields = ['gender', 'postcode', 'treated_eye']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        response = super(PatientCreateView, self).form_valid(form)
        return response

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientCreateView, self).dispatch(request, *args, **kwargs)

class PatientDeleteView(DeleteView):
    context_object_name = 'patient'
    success_url = '/cndapp/list/'

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientDeleteView, self).dispatch(request, *args, **kwargs)

class PreOpAssessmentCreateView(CreateView):
    model = PreOpAssessment
    form_class = PreOpAssessmentForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.patient = get_object_or_404(Patient, pk=self.kwargs['patient'])
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        va_form = PreOpAssessmentVisualAcuityReadingFormSet()
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form, va_form=va_form))

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
        va_form = PreOpAssessmentVisualAcuityReadingFormSet(self.request.POST)
        if (form.is_valid() and va_form.is_valid()):
            return self.form_valid(form, va_form)
        else:
            return self.form_invalid(form, va_form)

    def form_valid(self, form, va_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.patient = self.patient
        self.object = form.save()
        va_form.instance = self.object
        va_form.save()
        if 'save_and_next' in form.data:
            redirect = reverse('create_opnote', kwargs={'patient': self.patient.id})
        else:
            redirect = self.get_success_url()
        return HttpResponseRedirect(redirect)

    def form_invalid(self, form, va_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form, va_form=va_form))

class OpNoteCreateView(CreateView):
    model = OpNote
    form_class = OpNoteForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.patient = get_object_or_404(Patient, pk=self.kwargs['patient'])
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form))

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
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.instance.patient = self.patient
        self.object = form.save()
        if 'save_and_next' in form.data:
            redirect = reverse('create_followup', kwargs={'patient': self.patient.id})
        else:
            redirect = self.get_success_url()
        return HttpResponseRedirect(redirect)

    def form_invalid(self, form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(patient=self.patient, form=form))

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
