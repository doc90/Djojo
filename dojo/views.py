from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import DeleteView
from django.views import generic
from .forms import NinjaForm, MentorForm, EventForm, SkillForm
from django.http import HttpResponseRedirect

from .models import Ninja, Event, Mentor, Skill

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

    return render_to_response('dojo/ninja/ninja_list.html', {"ninja_list": ninja_list}, context_instance=RequestContext(request))


@permission_required('dojo.add_ninja', raise_exception=True)
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
    return render_to_response("dojo/ninja/ninja_add.html", {'form' : form }, context_instance=RequestContext(request))


@permission_required('dojo.change_ninja', raise_exception=True)
def ninja_edit(request, pk):
    instance = get_object_or_404(Ninja, pk=pk)
    if request.method == "POST":
        form = NinjaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/ninja/")
    else:
        form = NinjaForm(instance=instance)
    return render_to_response("dojo/ninja/ninja_edit.html", {'form' : form }, context_instance=RequestContext(request))
        
        
class Ninja_delete(DeleteView):
    model = Ninja
    success_url = '/dojo/ninja/'
    template_name = 'dojo/ninja/ninja_delete.html'
    
    def dispatch(self, *args, **kwargs):
        return super(Ninja_delete, self).dispatch(*args, **kwargs)


class Ninja_detail(generic.DetailView):
    model = Ninja
    template_name = 'dojo/ninja/ninja_detail.html'


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

    return render_to_response('dojo/mentor/mentor_list.html', {"mentor_list": mentor_list}, context_instance=RequestContext(request))


@permission_required('dojo.add_mentor', raise_exception=True)
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
    return render_to_response("dojo/mentor/mentor_add.html", {'form' : form }, context_instance=RequestContext(request))


@permission_required('dojo.change_mentor', raise_exception=True)
def mentor_edit(request, pk):
    instance = get_object_or_404(Mentor, pk=pk)
    if request.method == "POST":
        form = MentorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/mentor/")
    else:
        form = MentorForm(instance=instance)
    return render_to_response("dojo/mentor/mentor_edit.html", {'form' : form }, context_instance=RequestContext(request))


class Mentor_delete(DeleteView):
    model = Mentor
    success_url = '/dojo/mentor/'
    template_name = 'dojo/mentor/mentor_delete.html'
    
    def dispatch(self, *args, **kwargs):
        return super(Mentor_delete, self).dispatch(*args, **kwargs)


@permission_required('dojo.view_event', raise_exception=True)
def event_list(request):

    event_list = Event.objects.order_by('-pub_date')
    paginator = Paginator(event_list, 25)

    page = request.GET.get('page')
    try:
        event_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        event_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        event_list = paginator.page(paginator.num_pages)

    return render_to_response('dojo/event/event_list.html', {"event_list": event_list}, context_instance=RequestContext(request))


@permission_required('dojo.add_event', raise_exception=True)
def event_add(request):
    if request.method == 'POST':
        form = EventForm(data=request.POST)

        if form.is_valid():

            model_instance = form.save(commit=False)
            model_instance.slug = '%s%s%s' % (
                model_instance.pub_date.day, model_instance.pub_date.month, model_instance.pub_date.year
            )
            model_instance.save()
            return HttpResponseRedirect("/dojo/event/")
    else:
        form = EventForm()
    return render_to_response("dojo/event/event_add.html", {'form' : form }, context_instance=RequestContext(request))


@permission_required('dojo.change_event', raise_exception=True)
def event_edit(request, pk):
    instance = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/event/")
    else:
        form = EventForm(instance=instance)
    return render_to_response("dojo/event/event_edit.html", {'form' : form }, context_instance=RequestContext(request))


class Event_delete(DeleteView):
    model = Event
    success_url = '/dojo/event/'
    template_name = 'dojo/event/event_delete.html'

    def dispatch(self, *args, **kwargs):
        return super(Event_delete, self).dispatch(*args, **kwargs)

class Event_detail(generic.DetailView):
    model = Event
    template_name = 'dojo/event/event_detail.html'


@permission_required('dojo.view_skill', raise_exception=True)
def skill_list(request):

    skill_list = Skill.objects.order_by('title')
    paginator = Paginator(skill_list, 25)

    page = request.GET.get('page')
    try:
        skill_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        skill_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        skill_list = paginator.page(paginator.num_pages)

    return render_to_response('dojo/skill/skill_list.html', {"skill_list": skill_list}, context_instance=RequestContext(request))


@permission_required('dojo.add_skill', raise_exception=True)
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(data=request.POST)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect("/dojo/skill/")
    else:
        form = SkillForm()
    return render_to_response("dojo/skill/skill_add.html", {'form' : form }, context_instance=RequestContext(request))


@permission_required('dojo.change_skill', raise_exception=True)
def skill_edit(request, pk):
    instance = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dojo/skill/")
    else:
        form = SkillForm(instance=instance)
    return render_to_response("dojo/skill/skill_edit.html", {'form' : form }, context_instance=RequestContext(request))


class Skill_delete(DeleteView):
    model = Skill
    success_url = '/dojo/skill/'
    template_name = 'dojo/skill/skill_delete.html'

    def dispatch(self, *args, **kwargs):
        return super(Skill_delete, self).dispatch(*args, **kwargs)