from django.db import models

# Create your models here.
class Media(models.Model):
    image_url = models.URLField(max_length=200)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.IntegerField()

class Comment(models.Model):
    text = models.TextField()
    from_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey('Media', on_delete=models.CASCADE)