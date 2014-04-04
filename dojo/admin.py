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

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dettagli evento', {'fields':['pub_date', 'title', 'partecipants', 'notes']}),
    ]
    
    # inlines = ['pub_date','title']
    filter_horizontal = ['partecipants']
    list_display = ('pub_date', 'title')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Event, EventAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail')


admin.site.register(Level, LevelAdmin)


class MentorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Anagrafica', {'fields':['name', 'surname', 'email', 'cellphone']}),
        ('Note', {'fields':['notes']}),
    ]
    
admin.site.register(Mentor, MentorAdmin)