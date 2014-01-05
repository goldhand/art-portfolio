from django.conf.urls import patterns, url
from .views import IndexView


urlpatterns = patterns('pages.views',
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^feedback/$', 'feedback', name='feedback'),
	)