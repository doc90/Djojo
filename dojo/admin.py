from django.contrib import admin
from dojo.models import Ninja, Event, Level, Mentor

class NinjaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Anagrafica', {'fields':['name', 'surname', 'birthday', 'parentpermission', 'email', 'cellphone', 'photo', 'level']}),
        ('Contatti genitori', {'fields':['parentname', 'parentsurname', 'parentemail', 'parentcellphone'], 'classes':['collapse']}),
        ('Note', {'fields':['notes']}),
    ]
    
    list_display = ('name', 'surname', 'getAge', 'level', 'parentpermission')
    list_filter = ['level', 'parentpermission']
    search_fields = ['name', 'surname']

admin.site.register(Ninja, NinjaAdmin)

admin.site.register(Event)

admin.site.register(Level)


class MentorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Anagrafica', {'fields':['name', 'surname', 'email', 'cellphone']}),
        ('Note', {'fields':['notes']}),
    ]
    
admin.site.register(Mentor, MentorAdmin)