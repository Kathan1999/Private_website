from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title