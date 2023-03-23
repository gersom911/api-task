from django.db import models

class Task (models.Model):
    title = models.CharField(max_length=250,)# null =True,blank = True
    description = models.TextField(blank = True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    

