from django.contrib import admin
from .models import BlogSettings, Post
# Register your models here.

# admin.site.register(Post)
# admin.site.register(BlogSettings)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'status', 'created_on']
    prepopulated_fields = {'slug' : ('title',)}


@admin.register(BlogSettings)
class BlogSettings(admin.ModelAdmin):
    list_display = ['title',]