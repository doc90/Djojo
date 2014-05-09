from django.contrib import admin
from dojo.models import Ninja, Event, Level, Mentor

admin.site.register(Ninja)

admin.site.register(Event)

admin.site.register(Level)


class MentorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Anagrafica', {'fields':['name', 'surname', 'email', 'cellphone']}),
        ('Note', {'fields':['notes']}),
    ]
    
admin.site.register(Mentor, MentorAdmin)