from django.db import models
from django.contrib.auth.models import User


class MainTopic(models.Model):
    """A main topic"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Topic(models.Model):
    """A topic the user is learning about"""
    main_topic = models.ForeignKey(MainTopic, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
    

class Students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.CharField(max_length=200)

