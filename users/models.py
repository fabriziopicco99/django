from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    email = models.EmailField(default='')
    name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.image.url