from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length = 100)
    role = models.CharField(max_length=50)  
    team = models.CharField(max_length=50)
    batting_type = models.CharField(max_length = 50)
    bowling_type = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='player_images/')
    CATEGORY_CHOICES = [
        ('A', 'Category A'),
        ('B', 'Category B'),
        ('C', 'Category C'),
        ('D', 'Category D'),
    ]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='')

    def __str__(self):
        return self.name
