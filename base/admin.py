from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "created_at"]

class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like, LikeAdmin)
