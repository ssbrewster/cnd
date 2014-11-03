from django.conf.urls import patterns, url
from cndapp.views import *

urlpatterns = patterns('cndapp.views',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^contact/$', ContactView.as_view(), name='contact'),
                       url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
                       url(r'^about/$', AboutView.as_view(), name='about'),
                       url(r'^help/$', HelpView.as_view(), name='help'),
)
