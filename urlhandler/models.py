from django.db import models

# Create your models here.

class Shorturl(models.Model):

    original_url = models.URLField(max_length=100000 , blank=False)
    short_url = models.CharField(max_length=10 , blank=False , unique=True )

    def __str__(self):
        return self.short_url
    
