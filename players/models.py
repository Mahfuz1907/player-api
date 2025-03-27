from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length = 100)
    role = models.CharField(max_length=50)  # e.g., Batsman, Bowler
    team = models.CharField(max_length=50)
    batting_type = models.CharField(max_length = 50)
    bowling_type = models.CharField(max_length = 50)
    jersey = models.IntegerField()
    image = models.ImageField(upload_to='player_images/')

    def __str__(self):
        return self.name
