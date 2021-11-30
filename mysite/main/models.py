from django.db import models

# Create your models here.

class Curiosities(models.Model):
    id = models.AutoField(primary_key=True)
    curiosity = models.TextField()
    published_date = models.DateTimeField("date published")

    #override to print statement
    def __str__(self):
        return self.curiosity

class Vote(models.Model):
    
    vote_id = models.AutoField(primary_key=True)
    published_date = models.DateTimeField("date published")
    curiosity_id = models.ForeignKey(Curiosities, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(Curiosities, on_delete=models.CASCADE)

class Comment(models.Model):
    
    comment_id = models.AutoField(primary_key=True)
    text = models.TextField()
    published_date = models.DateTimeField("date published")
    curiosity_id = models.ForeignKey(Curiosities, on_delete=models.CASCADE)
    
class Category(models.Model):
    
    category_id = models.AutoField(primary_key=True)
    name = models.TextField()

