from django.conf.urls import patterns, url

from engine import views

urlpatterns = patterns('',
    url(r'^$',views.home, name='home'),
    url(r'^users/$', views.profile, name='profile'),
)

