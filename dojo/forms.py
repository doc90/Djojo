from django.forms import ModelForm, Textarea, TextInput
from .models import Ninja, Mentor

class NinjaForm(ModelForm):
    class Meta:
        model = Ninja
        fields = ['name', 'surname', 'birthday', 'parentpermission', 'email', 'cellphone', 'photo', 'level', 'parentname', 'parentsurname', 'parentemail', 'parentcellphone', 'notes']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'surname', 'email', 'cellphone', 'notes']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }