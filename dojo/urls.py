from django.contrib.auth.decorators import permission_required
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^ninja/$',views.ninja_list, name='ninja_list'),
    url(r'^ninja/new/$', views.ninja_add, name='ninja_add'),
    url(r'^ninja/(?P<pk>\d+)/edit/$', views.ninja_edit, name="ninja_edit"),
    url(r'^ninja/(?P<pk>\d+)/delete/$', permission_required('dojo.delete_ninja', raise_exception=True)(views.Ninja_delete.as_view()), name="ninja_delete"),
    url(r'^ninja/(?P<pk>\d+)/$', permission_required('dojo.view_ninja', raise_exception=True)(views.Ninja_detail.as_view()), name='ninja_detail'),
    
    url(r'^mentor/$',views.mentor_list, name='mentor_list'),
    url(r'^mentor/new/$', views.mentor_add, name='mentor_add'),
    url(r'^mentor/(?P<pk>\d+)/edit/$', views.mentor_edit, name="mentor_edit"),
    url(r'^mentor/(?P<pk>\d+)/delete/$', permission_required('dojo.delete_mentor', raise_exception=True)(views.Mentor_delete.as_view()), name="mentor_delete"),
    #url(r'^(?P<slug>.*)/$', views.detail, name='detail'),

    url(r'^event/$',views.event_list, name='event_list'),
    url(r'^event/new/$', views.event_add, name='event_add'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name="event_edit"),
    url(r'^event/(?P<pk>\d+)/delete/$', permission_required('dojo.delete_event', raise_exception=True)(views.Event_delete.as_view()), name="event_delete"),
    url(r'^event/(?P<pk>\d+)/$', permission_required('dojo.view_event', raise_exception=True)(views.Event_detail.as_view()), name='event_detail'),

)