from django.conf import settings
 
def global_settings(request):
    return {
            'VERSION': settings.VERSION,
            }
