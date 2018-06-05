from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
import datetime
import os
HOME_CHOICE = (
    (1, 'Monolite'),
    (2, 'Brick'),
    (3, 'Clay'),
)

class Home_buyer(models.Model):


    home_description = models.CharField(max_length = 200)
    home_room = models.IntegerField(default = 1)
    home_price_start = models.IntegerField(default = 0)
    home_price_finish = models.IntegerField(default=1000000)
    home_type = MultiSelectField(max_length = 50, choices = HOME_CHOICE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.home_description
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Comment(models.Model):
    home = models.ForeignKey(Home_buyer, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.comment_text