from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from .forms import NinjaForm, MentorForm
from django.http import HttpResponseRedirect

from dojo.models import Ninja, Event, Mentor

@permission_required('dojo.view_ninja', raise_exception=True)
def ninja_list(request):
    
    ninja_list = Ninja.objects.order_by('surname')
    paginator = Paginator(ninja_list, 25)
    
    page = request.GET.get('page')
    try:
        ninja_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ninja_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ninja_list = paginator.page(paginator.num_pages)

    return render_to_response('ninja/ninja_list.html', {"ninja_list": ninja_list}, context_instance=RequestContext(request))


@permission_required('dojo.can_add_ninja', raise_exception=True)
def ninja_add(request):
    if request.method == 'POST':
        form = NinjaForm(data=request.POST)
        
        if form.is_valid():
            
            model_instance = form.save(commit=False)
            model_instance.slug = '%s%s' % (
                model_instance.name, model_instance.surname
            )
            model_instance.save()
            return HttpResponseRedirect("/dojo/ninja/")
    else:
        form = NinjaForm()
    return render_to_response("ninja/ninja_form.html", {'form' : form }, context_instance=RequestContext(request))

@permission_required('dojo.view_mentor', raise_exception=True)
def mentor_list(request):
    
    mentor_list = Mentor.objects.order_by('surname')
    paginator = Paginator(mentor_list, 25)
    
    page = request.GET.get('page')
    try:
        mentor_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mentor_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mentor_list = paginator.page(paginator.num_pages)

    return render_to_response('mentor/mentor_list.html', {"mentor_list": mentor_list}, context_instance=RequestContext(request))


@permission_required('dojo.can_add_mentor', raise_exception=True)
def mentor_add(request):
    if request.method == 'POST':
        form = MentorForm(data=request.POST)
        
        if form.is_valid():
            
            model_instance = form.save(commit=False)
            model_instance.slug = '%s%s' % (
                model_instance.name, model_instance.surname
            )
            model_instance.save()
            return HttpResponseRedirect("/dojo/mentor/")
    else:
        form = MentorForm()
    return render_to_response("mentor/mentor_form.html", {'form' : form }, context_instance=RequestContext(request))


