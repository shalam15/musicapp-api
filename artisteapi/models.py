from django.db import models
from django.urls import reverse

musicGenre= (
    
        'hipHop',
        'pop',
)


class Artiste(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    worldRank = models.IntegerField()
    musicGenre = musicGenre
    origin = models.CharField(max_length=120)
    originFlag = models.CharField(max_length=120)

    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    
    #show title as the obejct
    def __str__(self):
        return self.firstName  
