from django.conf.urls import patterns , url
from polls import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^index/' , TemplateView.as_view(template_name='index.html'),),
	url(r'^list/' , views.poll_list , name = 'poll_list',),
	url(r'^poll/(?P<poll_id>\d+)/$', views.poll_details , name='poll_details',),

]