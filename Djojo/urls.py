from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView
from engine.views import UserProfileDetailView
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^users/', include('registration.backends.simple.urls')),
    
    url(r'^$','engine.views.home', name='home'),
    url(r'^dojo/', include('dojo.urls'), name='dojo'),
    url(r'^documents/', include('documents.urls', namespace='documents'), name='documents'),
    
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
    
    #fix per django 1.6
    #http://stackoverflow.com/questions/19985103/
    url(r'^password/change/$', auth_views.password_change, name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    
    url(r'^users/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
)


urlpatterns += patterns('',
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    # {'document_root': settings.MEDIA_ROOT}),
    #{'document_root': settings.MEDIA_ROOT, 'show_indexes': True},
    {'document_root': settings.STATIC_ROOT, 'show_indexes': True})
)

handler403 = 'engine.views.custom403'

