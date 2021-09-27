from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default='#FFF2A7')
    def __str__(self):
        return '{0}. {1}'.format(self.id,self.name)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0}. {1}'.format(self.id,self.title)