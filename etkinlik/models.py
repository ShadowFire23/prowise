from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=170)
    exp = models.CharField(max_length=200)
    event_date = models.DateField(blank=True, null=True)
    detail = models.TextField()
    status = models.BooleanField(default=False)
    img_event = models.ImageField()
    url_sistem = models.SlugField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
