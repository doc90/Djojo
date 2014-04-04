from django.contrib.auth.decorators import permission_required
from django.conf.urls import patterns, url

from dojo import views

urlpatterns = patterns('',
    url(r'^ninja/$',views.ninja_list, name='ninja_list'),
    url(r'^ninja/new/$', views.ninja_add, name='ninja_add'),
    url(r'^ninja/edit/(?P<pk>\d+)/$', views.ninja_edit, name="ninja_edit"),
    url(r'^ninja/delete/(?P<pk>\d+)/$', permission_required('dojo.can_delete_ninja', raise_exception=True)(views.Ninja_delete.as_view()), name="ninja_delete"),
    
    
    url(r'^mentor/$',views.mentor_list, name='mentor_list'),
    url(r'^mentor/new/$', views.mentor_add, name='mentor_add'),
    url(r'^mentor/edit/(?P<pk>\d+)/$', views.mentor_edit, name="mentor_edit"),
    url(r'^mentor/delete/(?P<pk>\d+)/$', permission_required('dojo.can_delete_mentor', raise_exception=True)(views.Mentor_delete.as_view()), name="mentor_delete"),
    #url(r'^(?P<slug>.*)/$', views.detail, name='detail'),
)