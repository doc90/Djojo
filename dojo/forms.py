from django.forms import ModelForm
from .models import Ninja, Mentor

class NinjaForm(ModelForm):
    class Meta:
        model = Ninja
        fields = ['name', 'surname', 'birthday', 'parentpermission', 'email', 'cellphone', 'photo', 'level', 'parentname', 'parentsurname', 'parentemail', 'parentscellphone', 'notes']

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'surname', 'email', 'cellphone', 'notes']
