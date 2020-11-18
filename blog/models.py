from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    meta = models.CharField(max_length=85)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    top_photo = models.ImageField()
    url_sistem = models.SlugField(blank=True, null=True)
    status = models.BooleanField(default=False)
    news = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title

class Comment(models.Model):
    yazan = models.CharField(max_length=50)
    emmail = models.EmailField()
    yorum = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.yazan
