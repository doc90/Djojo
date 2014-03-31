from django.contrib import admin
from dojo.models import Ninja, Event

class NinjaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Anagrafica', {'fields':['name','surname','age','parentspermission']}),
        ('Contatti', {'fields':['email','cellphone','parentscellphone']}),
        ('Note',{'fields':['notes']}),
    ]
    
    list_display = ('name','surname','age','parentspermission')
    search_fields = ['name','surname']

admin.site.register(Ninja, NinjaAdmin)

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dettagli evento', {'fields':['pub_date','title','partecipants','notes']}),
    ]
    
    #inlines = ['pub_date','title']
    filter_horizontal = ['partecipants']
    list_display = ('pub_date','title')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Event, EventAdmin)
