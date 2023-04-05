from django.contrib.auth.models import User
from django.db import models


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    points = models.IntegerField(default=0)
    event_id = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
