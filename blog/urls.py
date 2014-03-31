from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<slug>.*)/$', views.detail, name='detail'),
)