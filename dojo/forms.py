from django.forms import ModelForm, Textarea, ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Ninja, Mentor, Event

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


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'pub_date', 'participants', 'mentors', 'location', 'notes', 'activity']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'activity': Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }