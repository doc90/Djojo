from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    title = models.CharField('Titolo', max_length=150)
    uploadedfile = models.FileField(upload_to='./documents')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title