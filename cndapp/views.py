from django.views.generic import TemplateView, FormView
from cndapp.forms import *

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
