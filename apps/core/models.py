from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.manager import ManagerDescriptor
# Rich text fields that do not support file upload
from ckeditor.fields import RichTextField
# Rich text field that supports file upload
from ckeditor_uploader.fields import RichTextUploadingField
import readtime 

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    post_thum = models.ImageField(null=True, blank=True, upload_to="images/thumbnails")
    post_banner = models.ImageField(null=True, blank=True, upload_to="images/banners")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    synopsis = RichTextUploadingField(max_length=300, blank = True, null= True)
    content = RichTextUploadingField(blank = True, null= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text 


class BlogSettings(models.Model):
    title = models.CharField(max_length=200, unique=True)
    heading = models.CharField(max_length=200, unique=True)
    pro_image = models.ImageField(null=True, blank=True, upload_to="images/")
    short_intro = models.TextField()
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    stackoverflow_link = models.CharField(max_length=200, null=True, blank=True)
    codepen_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

