from django.db import models

class DestekKonu(models.Model):
    konu = models.CharField(max_length=200)

    def __str__(self):
        return self.konu

class Contact(models.Model):
    title = models.CharField(max_length=200)
    sender = models.CharField(max_length=100)
    mail = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.title

class Support(models.Model):
    subject = models.ForeignKey(DestekKonu, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=200)
    sender = models.CharField(max_length=100)
    mail = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.title
