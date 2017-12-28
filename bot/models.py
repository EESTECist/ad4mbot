from django.db import models

# Create your models here.
class Message(models.Model):
    body = models.TextField()
    is_bot = models.BooleanField(default=0)
