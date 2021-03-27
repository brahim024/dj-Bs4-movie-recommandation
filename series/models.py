from django.db import models
from .scraper import get_series
# Create your models here

# Create your models here.
class Serie(models.Model):
    name=models.CharField(max_length=30,blank=True)
    url=models.URLField()
    #years=models.CharField(max_length=100,blank=True)
    #actor_list=models.CharField(max_length=100,blank=True)
    rating=models.CharField(max_length=2,blank=100)
    image=models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        titles,rating,img=get_series(self.url)
        self.name=titles
        #self.years=years
        #self.actor_list=actor_list
        self.rating=rating
        self.image=img
        super().save(*args,**kwargs)
        
