from django.db import models
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=280)
    created_datetime = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    is_boast = models.BooleanField(default=False)
    post_id = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return '{}: {}'.format(self.content, self.created_datetime)
