from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    #task is owned by a specific user

    user = models.ForeignKey(User,on_delete= models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length= 100)
    description = models.TextField(blank= True)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now= True)

    def __str__(self):

        return self.title
    
    class Meta:

        ordering = ['complete']
