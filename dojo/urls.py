from django.conf.urls import patterns, url

from dojo import views

urlpatterns = patterns('',
    url(r'^ninja/$',views.ninja_list, name='ninja_list'),
    url(r'^ninja/new/$', views.ninja_add, name='ninja_add'),
    
    url(r'^mentor/$',views.mentor_list, name='mentor_list'),
    url(r'^mentor/new/$', views.mentor_add, name='mentor_add'),
    #url(r'^(?P<slug>.*)/$', views.detail, name='detail'),
)