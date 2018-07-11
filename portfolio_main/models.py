from django.db import models
import datetime



class resume(models.Model):
    cat_choices = (
        ("PYTHON","PYTHON"),
        ("HTLM","HTML"),
        ("BLENDER","BLENDER"),
    )

    category = models.CharField(max_length = 7 , choices = cat_choices , default = "HTML")
    title = models.CharField(max_length = 30)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    article_image = models.ImageField()

    def __str__(self):
        return self.title



