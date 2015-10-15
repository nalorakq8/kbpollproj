from django.shortcuts import render
from django.http import Http404
from .models import Poll
from django.shortcuts import get_list_or_404, get_object_or_404


def poll_list(request):
	
	qs = get_list_or_404(Poll)
	return render(request , "poll_list.html" , {"polls" : qs})
def poll_details (request , poll_id):
	
	poll = get_object_or_404(Poll , pk=poll_id)
	
	return render(request , "poll_details.html", {"polls": poll })

# its better to use get_list_or_404 and get_object_or_404 becuase its more efficent and looks better
# and you dont need to use try to get the expected error