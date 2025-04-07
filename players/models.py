from django.db import models
from django.core.exceptions import ValidationError

class Head(models.Model):
    name = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='player_images/', default='player-img/logo.png')
    description = models.CharField(max_length=500, default='')


    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, default='')
    short_name = models.CharField(max_length=5, default='')
    image = models.ImageField(upload_to='player_images/', default='player-img/logo.png')
    details = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class Category(models.Model):
    Category_Choices = [
        ('A', 'Category A'),
        ('B', 'Category B'),
        ('C', 'Category C'),
    ]
    name = models.CharField(max_length=1, choices=Category_Choices, default=0)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length = 100)

    role_choices = [
        ('Batsman', 'Batsman'), ('Wicket Keeper Batsman', 'Wicket Keeper Batsman'), ('Bowler', 'Bowler'), ('Batting All-rounder', 'Batting All-rounder'), ('Bowling All-rounder', 'Bowling All-rounder')
    ]
    role = models.CharField(max_length=100, choices=role_choices, default='') 

    country_choices = [
        ('Pakistan', 'Pakistan'), ('Bangladesh', 'Bangladesh')
    ] 
    country = models.CharField(max_length=100, choices=country_choices, default='')

    batting_type_choice = [
        ('Right Arm Batsman', 'Right Arm Batsman'), ('Left Arm Batsman', 'Left Arm Batsman')
    ]
    batting_type = models.CharField(max_length=100, choices=batting_type_choice, default='')

    bowling_type_choice = [
       ('None', 'None'), ('Right Arm Fast', 'Right Arm Fast'), ('Left Arm Fast', 'Left Arm Fast'),
       ('Right Arm Medium', 'Right Arm Medium'), ('Left Arm Medium', 'Left Arm Medium'),
        ('Right Arm Off Spin', 'Right Arm Off Spin'), ('Left Arm Off Spin', 'Left Arm Off Spin'), 
        ('Right Arm Leg Spin', 'Right Arm Leg Spin'), ('Left Arm Leg Spin', 'Left Arm Leg Spin')
    ]
    bowling_type = models.CharField(max_length=100, choices=bowling_type_choice, default='')

    image = models.ImageField(upload_to='player_images/')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players", null=True, blank=True)
    

    def __str__(self):
        return self.name
