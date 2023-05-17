from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    
    def __str__(self):
        return self.title
