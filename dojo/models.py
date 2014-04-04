import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from dateutil.relativedelta import relativedelta
from tinymce.models import HTMLField
from django.forms.forms import BoundField

class Level(models.Model):
    
    title = models.CharField('Titolo', max_length=100)
    image = models.ImageField('Immagine', upload_to='.', blank=True)
    value = models.IntegerField('Valore')
    
    def __unicode__(self):
        return self.title
    
    def thumbnail(self):
        return u'<img src="%s" />' % (self.image.url)
    thumbnail.short_description = 'Immagine'
    thumbnail.allow_tags = True

class Ninja(models.Model):
    name = models.CharField('Nome', max_length=50)
    surname = models.CharField('Cognome', max_length=50)
    birthday = models.DateField('Data di nascita', blank=True, null=True)
    photo = models.ImageField('Foto', upload_to='.', blank=True)
    level = models.ForeignKey(Level, null=True, blank=True)
    cellphone = models.IntegerField('Cellulare', null=True, blank=True)
    email = models.EmailField('Email', blank=True)
    parentpermission = models.BooleanField('Manleva', default=False)
    parentname = models.CharField('Nome Genitore', max_length=50, blank=True)
    parentsurname = models.CharField('Cognome Genitore', max_length=50, blank=True)
    parentemail = models.EmailField('Email', blank=True)
    parentscellphone = models.IntegerField('Cell Genitore', null=True, blank=True)
    notes = HTMLField('Note', blank=True)   
    slug = models.CharField(max_length=200)
    
    def getAge(self):
        return relativedelta(datetime.date.today(), self.birthday).years
    getAge.short_description = 'Eta'
    getAge.integer = True
    
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
    notes = HTMLField('Note', blank=True)
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
        
class Mentor(models.Model):
    name = models.CharField('Nome', max_length=50)
    surname = models.CharField('Cognome', max_length=50)
    birthday = models.DateField('Data di nascita', blank=True, null=True)
    cellphone = models.IntegerField('Cellulare', null=True, blank=True)
    email = models.EmailField('Email', blank=True)
    notes = HTMLField('Note', blank=True)   
    slug = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name + ' ' + self.surname
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = '%s%s' % (
                self.name, self.surname
            )
        super(Mentor, self).save(*args, **kwargs)

