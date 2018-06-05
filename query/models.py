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
def get_image_path(instance,filename):
    return os.path.join('photo', str(instance.id), filename)
class Home(models.Model):

    home_title = models.CharField(max_length = 100)
    home_description = models.CharField(max_length = 200)
    home_room = models.IntegerField(default = 1)
    home_price = models.IntegerField(default = 0)
    home_type = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    home_image = models.ImageField(upload_to = get_image_path, blank = True, null = True, default = None)
    def __str__(self):
        return self.home_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Comment(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.comment_text