from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateField(auto_now_add = True)
    author = models.CharField(max_length = 50, null = True)
    image = models.ImageField(("image/"), upload_to=None, height_field=500, width_field=500, max_length=500, blank = True)
