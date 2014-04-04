from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import NinjaForm, MentorForm
from django.http import HttpResponseRedirect

from .models import Ninja, Event, Mentor

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


@permission_required('dojo.can_edit_ninja', raise_exception=True)
def ninja_edit(request, pk):
    instance = get_object_or_404(Ninja, pk=pk)
    if request.method == "POST":
        form = NinjaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/ninja/")
    else:
        form = NinjaForm(instance=instance)
    return render_to_response("ninja/ninja_edit.html", {'form' : form }, context_instance=RequestContext(request))    
        
        
class Ninja_delete(DeleteView):
    model = Ninja
    success_url = 'dojo/ninja/'
    template_name = 'ninja/ninja_delete.html'
    
    def dispatch(self, *args, **kwargs):
        return super(Ninja_delete, self).dispatch(*args, **kwargs)


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


@permission_required('dojo.can_edit_mentor', raise_exception=True)
def mentor_edit(request, pk):
    instance = get_object_or_404(Mentor, pk=pk)
    if request.method == "POST":
        form = MentorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/mentor/")
    else:
        form = MentorForm(instance=instance)
    return render_to_response("mentor/mentor_edit.html", {'form' : form }, context_instance=RequestContext(request))    


class Mentor_delete(DeleteView):
    model = Mentor
    success_url = '/dojo/mentor/'
    template_name = 'mentor/mentor_delete.html'
    
    def dispatch(self, *args, **kwargs):
        return super(Mentor_delete, self).dispatch(*args, **kwargs)
