from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView


def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'engine/home.html')
    return login(request, template_name='engine/home.html')

@login_required
def profile(request):
    return render(request, template_name='engine/profile.html')

def custom403(request):
    return render(request, template_name='engine/403.html')


class MyRegistrationView(RegistrationView):
    success_url='/'
    def get_success_url(self, request, user):
        return "/upload/new"