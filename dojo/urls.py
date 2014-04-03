from django.conf.urls import patterns, url

from dojo import views

urlpatterns = patterns('',
    url(r'^ninja/$',views.ninjalist, name='ninjalist'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>.*)/$', views.detail, name='detail'),
)