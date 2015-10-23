from django.conf.urls import patterns , url
from polls import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^index/' , TemplateView.as_view(template_name='index.html'),),
	url(r'^list/' , views.PollList.as_view() , name = 'poll_list',),
	url(r'^poll/(?P<pk>[0-9]+)/$', views.PollDetails.as_view() , name='poll_details',),
	url(r'^last/' , views.last_updated_polls.as_view() , name = 'last_updated_polls',),
	url(r'^search/(?P<word>[\w-]+)/$', views.search_word.as_view() , name='search_word',),
	url(r'^duplicate/(?P<id>[\d+]+)/$', views.duplicate.as_view() , name='duplicate',),

]