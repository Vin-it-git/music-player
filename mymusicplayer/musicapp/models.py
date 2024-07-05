from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='music/')
    
    def __str__(self):
        return self.title