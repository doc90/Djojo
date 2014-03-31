import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
# from tinymce.models import HTMLField

class Ninja(models.Model):
    name = models.CharField('Nome', max_length=200)
    surname = models.CharField('Cognome', max_length=200)
    age = models.IntegerField('Eta')
    parentspermission = models.BooleanField('Manleva?',default=False)
    # notes = HTMLField('Note')
    email = models.EmailField('Email', blank=True)
    cellphone = models.IntegerField('Cellulare', null=True, blank=True)
    parentscellphone = models.IntegerField('Cell Genitori', null=True, blank=True)
    notes = models.TextField('Note', blank=True)   
    slug = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name + ' ' + self.surname
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = '%s%s' % (
                self.name, self.surname
            )
        super(Ninja, self).save(*args, **kwargs)
        
class Event(models.Model):
    title = models.CharField('Titolo', max_length=200)
    pub_date = models.DateField('Data evento')
    partecipants = models.ManyToManyField(Ninja, blank=True)
    partecipantsnumber = models.IntegerField()
    location = models.CharField('Luogo', max_length=200, blank=True)
    notes = models.TextField('Note', blank=True)
    slug = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.pub_date)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = '%s%s%s' % (
                self.pub_date.day, self.pub_date.month, self.pub_date.year
            )
            # a=Event.objects.get(pk=1)
            self.partecipantsnumber = 0
        super(Event, self).save(*args, **kwargs)
        
