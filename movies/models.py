from django.db import models
from .scrap import main
# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=30,blank=True)
    url=models.URLField()
    years=models.CharField(max_length=100,blank=True)
    actor_list=models.CharField(max_length=100,blank=True)
    rating=models.CharField(max_length=2,blank=100)
    image=models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        titles,years,rating,actor_list,img=main(self.url)
        self.name=titles
        self.years=years
        self.actor_list=actor_list
        self.rating=rating
        #self.image=img
        super().save(*args,**kwargs)
