from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
#create user model
class User(AbstractUser):
    pass

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    choices = (('team', 'Team'), ('solo', 'Solo'), ('both', 'Team/Solo'))
    team_type = models.CharField(max_length=4, choices=choices)
    team_size = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    depts = (
        ('cse', 'Computer Science'),
        ('ece', 'ECE'),
        ('eee', 'EEE'),
        ('mech', 'Mechanical'),
        ('civil', 'Civil'),
        ('chem', 'Chemical'),
        ('it', 'Information Technology'),
        ('bme', 'Biomedical Engineering')
    )
    dept = models.CharField(max_length=5, choices=depts)
    rounds = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    venue = models.CharField(max_length=100)
    date = models.DateField()
    first_prize = models.IntegerField(validators=[MinValueValidator(0)])
    second_prize = models.IntegerField(validators=[MinValueValidator(0)])
    third_prize = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title
    
class Round(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='all_rounds')

    def __str__(self):
        return "{0} - {1}".format(self.event.title, self.title)