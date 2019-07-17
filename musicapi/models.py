from django.db import models
from django.urls import reverse

class Music(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    image = models.CharField(max_length=120)
    lyrics = models.TextField()
    musicFile = models.CharField(max_length=120)
    dateCreated = models.CharField(max_length=120)

    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    
    #show title as the obejct
    def __str__(self):
        return self.title  
