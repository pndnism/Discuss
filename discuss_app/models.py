from django.db import models
from django.utils import timezone
from enum import Enum
import datetime

class ThemeGenre(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class DiscussTheme(models.Model):
    OPEN_DISCUSS = 'open'
    ACTIVE_DISCUSS = 'active'
    CLOSED_DISCUSS = 'closed'

    class DISCUSS_STATUS(Enum):
        open = ('o', 'Open')
        active = ('a', 'Active')
        closed = ('c', 'Closed')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    title = models.CharField(max_length=50)
    genre = models.ForeignKey(ThemeGenre, on_delete=models.CASCADE)
    status = models.CharField(
                        max_length=1,
                        choices=[x.value for x in DISCUSS_STATUS]
                    )
    create_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_date <= now

class DiscussSide(models.Model):
    discuss_theme =  models.ForeignKey(DiscussTheme, on_delete=models.CASCADE)
    max_n_of_member = models.IntegerField(default=5)
    one_side = models.CharField(max_length=25)
    one_side_count = models.IntegerField(default=0)
    another_side = models.CharField(max_length=25)
    another_side_count = models.IntegerField(default=0)
    create_date = models.DateTimeField('date published')
    



