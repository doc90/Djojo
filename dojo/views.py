from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from dojo.models import Ninja,Event

def eventindex(request):
    event_list = Event.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    
    page = request.GET.get('page')
    try:
        latest_event_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_event_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_event_list = paginator.page(paginator.num_pages)

    return render_to_response('blog/index.html', {"latest_event_list": latest_event_list})
