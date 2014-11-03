from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.sites.models import get_current_site
from cndapp.forms import *
from cndapp.models import Patient

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
        context['patient_url'] = 'http://' + get_current_site(self.request).domain + '/cndapp/uuid/' + self.get_object().uuid.lower()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PatientDetailView, self).dispatch(request, *args, **kwargs)

class PatientCreateView(CreateView):
    model = Patient
    fields = ['sex', 'dob_year']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        response = super(PatientCreateView, self).form_valid(form)
        return response
