from django.db import models
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.user')#ForeignKey - link to another model
    title=models.CharField(max_length=200)#CharFiled for limited number of characters
    text=models.TextField()#TextFiled for long text without a limit
    created_date=models.DateTimeField(default=timezone.now)#this a date time filed
    published_date=models.DateTimeField(blank=True, null=True)
#https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types (Django documentation for field types)

def publish(self):
    self.published_date=timezone.now()
    self.save()

def __str__(self):
    return self.title


# Create your models here.
