from django.contrib import admin
from .models import BlogSettings, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(BlogSettings)