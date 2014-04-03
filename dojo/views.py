from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import login

from dojo.models import Ninja, Event

@permission_required('dojo.view_ninja', raise_exception=True)
def ninjalist(request):
    
    ninja_list = Ninja.objects.order_by('surname')
    paginator = Paginator(ninja_list, 10)
    
    page = request.GET.get('page')
    try:
        latest_event_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_event_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ninja_list = paginator.page(paginator.num_pages)

    return render_to_response('ninja/ninjalist.html', {"ninja_list": ninja_list}, context_instance=RequestContext(request))
