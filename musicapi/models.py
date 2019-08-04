from django.db import models
from django.urls import reverse
from datetime import datetime 

musicGenre= (
    
       (1, 'hipop'),
        (2, 'afro'),
        (3, 'indie'),
        (4, 'k-pop'),
        (5, 'pop'),
)

class Music(models.Model):


    # id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    isExplicit = models.BooleanField(default=False)
    musicGenre = models.IntegerField(max_length=1, choices=musicGenre, default ="1")
    image = models.ImageField(upload_to = 'media/', default = 'media/defaults/no-img.jpg')
    lyrics = models.TextField()
    musicFile = models.FileField(upload_to='media/', default= 'media/defaults/Krazy-Rymz-My-Matter_1lzbZGR.mp3')
    dateCreated = models.DateTimeField(default=datetime.now, blank=True )

    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    
    #show title as the obejct
    def __str__(self):
        return self.title  
