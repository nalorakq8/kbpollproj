from django.shortcuts import render , redirect
from django.http import Http404
from .models import Poll , Survey
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView , DetailView
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class PollList(ListView):
	model = Poll
	template_name = "poll_list.html"
	context_object_name = "polls"
	
class last_updated_polls(ListView):
	model = Poll
	template_name = "poll_list.html"
	context_object_name = "polls"
	queryset = Poll.objects.order_by('-updated_at')[0:5]
class search_word(ListView):
	model = Poll
	template_name = "poll_list.html"
	context_object_name = "polls"
	#queryset = Poll.objects.filter(question__istartswith ="what")
	def get_queryset(self):
		word = self.kwargs['word']
		return Poll.objects.filter(Q(question__icontains = word) | 
			Q(name__icontains = word) | Q(category__icontains = word))
class duplicate(ListView):
	model = Poll
	template_name = "poll_details.html"
	context_object_name = "polls"
	
	def dispatch(self, *args, **kwargs):
		duplicate_from = self.kwargs['id']
		new_object = Poll.objects.get(pk=duplicate_from)
		new_object.pk = None
		new_object.save()
		return HttpResponseRedirect('/polls/poll/%s' %(new_object.pk))

class Survey(ListView):
	model = Survey
	template_name = "poll_list.html"
	context_object_name = "polls"
	#queryset = Survey.objects.filter(questions__choice__label__iexact = 'football')
	queryset = Survey.objects.filter(questions__choice__isnull = True)
		
	#we can use get_object to return single object the view will display
	#we can use get_context_data to return list of objects
	
class PollDetails(DetailView):
	model = Poll
	template_name = 'poll_details.html'
	context_object_name = 'polls'
def poll_list(request):
	
	qs = get_list_or_404(Poll)
	return render(request , "poll_list.html" , {"polls" : qs})
def poll_details (request , poll_id):
	
	poll = get_object_or_404(Poll , pk=poll_id)
	
	return render(request , "poll_details.html", {"polls": poll })

# its better to use get_list_or_404 and get_object_or_404 becuase its more efficent and looks better
# and you dont need to use try to get the expected error