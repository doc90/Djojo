from django.contrib.auth.decorators import permission_required
from django.conf.urls import patterns, url

from .views import Add_document, Edit_document, Delete_document, documents_list

urlpatterns = patterns('',
   url(r'^$', documents_list, name='list'),
   url(r'^new/$', Add_document.as_view(), name='add'),
   url(r'^(?P<pk>\d+)/edit/$', Edit_document.as_view(), name='edit'),
   url(r'^(?P<pk>\d+)/delete/$', Delete_document.as_view(), name='delete'),
)