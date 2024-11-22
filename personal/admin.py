from django.contrib import admin
from .models import Post

admin.site.register(Post)
class Blogpostadmin(admin.ModelAdmin):
    display = ('title','date')