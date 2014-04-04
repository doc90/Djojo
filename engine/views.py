from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from engine.models import UserProfile

def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'engine/home.html')
    return login(request, template_name='engine/home.html')

@login_required
def profile(request):
    return render(request, template_name='engine/profile.html')

def custom403(request):
    return render(request, template_name='engine/403.html')



class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "engine/profile.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user    