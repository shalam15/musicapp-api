from django.db import models
from django.urls import reverse
from musicapi.models import musicGenre

musicGenre= musicGenre

class Artiste(models.Model):
    # id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50, default="noname")
    lastName = models.CharField(max_length=50, default="noname")
    worldRank = models.IntegerField(default="1000000000")
    musicGenre = models.IntegerField(max_length=1, choices=musicGenre, default ="1")
    origin = models.CharField(max_length=120,default="noorigin")
    originFlag = models.ImageField(upload_to = 'media/', default = 'media/defaults/no-img.jpg')
    avatarImage = models.ImageField(upload_to = 'media/', default = 'media/defaults/avartar-default.png')

   

    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    
    #show title as the obejct
    def __str__(self):
        return self.firstName  
