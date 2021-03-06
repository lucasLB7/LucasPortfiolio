from django.db import models
import datetime
from cloudinary.models import CloudinaryField


class Resume(models.Model):
    cat_choices = (
        ("PYTHON","PYTHON"),
        ("HTML","HTML"),
        ("BLENDER","BLENDER"),
    )

    category = models.CharField(max_length = 7 , choices = cat_choices , default = "HTML")
    title = models.CharField(max_length = 30)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    githuburl = models.CharField(max_length = 255, blank = True)
    live_app_deployment = models.CharField(max_length = 255 , blank = True)
    article_image = CloudinaryField('image', blank = True)

    def __str__(self):
        return self.title

