from django.db import models

# Create your models here.

class Curiosities(models.Model):
    
    author_name = models.CharField(max_length=200)
    curiosity = models.TextField()
    published_date = models.DateTimeField("date published")
    

    #override to print statement
    def __str__(self):
        return self.curiosity
