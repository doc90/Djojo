from django.forms import ModelForm, Textarea
from .models import Ninja, Mentor, Event, Skill

class NinjaForm(ModelForm):
    class Meta:
        model = Ninja
        fields = ['name', 'surname', 'birthday', 'tutorpermission', 'email', 'cellphone', 'photo', 'photopermission', 'skills', 'tutorname', 'tutorsurname', 'tutoremail', 'tutorcellphone', 'notes']
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

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'color', 'notes']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }