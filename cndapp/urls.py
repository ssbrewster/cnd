from django.conf.urls import patterns, url
from cndapp.views import *

urlpatterns = patterns('cndapp.views',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'contact/$', ContactView.as_view(), name='contact'),
                       url(r'thanks/$', ThanksView.as_view(), name='thanks'),
                       url(r'about/$', AboutView.as_view(), name='about'),
                       url(r'help/$', HelpView.as_view(), name='help'),
                       url(r'patient/$', PatientListView.as_view(), name='list'),
                       url(r'patient/create/$', PatientCreateView.as_view(), name='create'),
                       url(r'patient/(?P<pk>\d+)/$', PatientDetailView.as_view(), name='detail'),
                       url(r'patient/uuid/(?P<uuid>.+)/$', PatientUUIDView.as_view(), name='uuid'),
                       url(r'patient/(?P<pk>\d+)/delete$', PatientDeleteView.as_view(), name='delete'),
                       url(r'patient/(?P<patient>\d+)/preop$', PreOpAssessmentCreateView.as_view(), name='create_preop'),
                       url(r'patient/(?P<patient>\d+)/opnote$', OpNoteCreateView.as_view(), name='create_opnote'),
                       url(r'patient/(?P<patient>\d+)/followup$', FollowUpCreateView.as_view(), name='create_followup'),
)