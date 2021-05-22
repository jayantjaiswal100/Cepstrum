from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='inplace', height_field=None, width_field=None, max_length=None)
    intro = RichTextField()
    article = RichTextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

