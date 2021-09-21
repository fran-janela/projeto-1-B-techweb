from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    # COLOR_CHOICES = [
    #     ("#FFFFFF", "white"),
    #     ("#000000", "black"),
    #     ("#FF0000", "red")
    # ]
    name = models.CharField(max_length=200)
    # color = ColorField(choices=COLOR_CHOICES)
    def __str__(self):
        return '{0}. {1}'.format(self.id,self.name)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0}. {1}'.format(self.id,self.title)