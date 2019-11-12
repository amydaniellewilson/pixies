from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    lyric = models.TextField()
    year = models.IntegerField()
    image = models.TextField()
    music = models.TextField()
    youtube = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.album} : {self.year}'
