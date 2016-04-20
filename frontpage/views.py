from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    context = {}
    return render_to_response('frontpage/base.html', context, context_instance=RequestContext(request))