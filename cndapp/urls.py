from django.conf.urls import patterns, url
from cndapp.views import *

urlpatterns = patterns('cndapp.views',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'contact/$', ContactView.as_view(), name='contact'),
                       url(r'thanks/$', ThanksView.as_view(), name='thanks'),
                       url(r'about/$', AboutView.as_view(), name='about'),
                       url(r'help/$', HelpView.as_view(), name='help'),
                       url(r'list/$', PatientListView.as_view(), name='list'),
                       url(r'create/$', PatientCreateView.as_view(), name='create'),
                       url(r'detail/(?P<pk>\d+)/$', PatientDetailView.as_view(), name='detail'),
                       url(r'^uuid/(?P<uuid>.+)/$', PatientUUIDView.as_view()),
                       url(r'delete/(?P<pk>\d+)/$', PatientDeleteView.as_view(), name='delete'),
                       url(r'create/preop/(?P<patient>\d+)$', PreOpAssessmentCreateView.as_view(), name='create_preop'),
                       url(r'create/opnote/(?P<patient>\d+)$', OpNoteCreateView.as_view(), name='create_opnote'),
                       url(r'create/followup/(?P<patient>\d+)$', FollowUpCreateView.as_view(), name='create_followup'),
)
