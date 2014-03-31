import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField('Titolo',max_length=200)
    content = HTMLField('Contenuto')
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Pubblicato il',default=datetime.datetime.now)
    
    def excerpt(self):
        maxChar=250
        if len(self.content)>maxChar:
            return self.content[:maxChar-3] + '...'
        else:
            return self.content[:maxChar]
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug= '%i%i%i/%s' % (
                self.pub_date.day, self.pub_date.month, self.pub_date.year, slugify(self.title)
            )
        super(Post, self).save(*args, **kwargs)