from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Blog_App.models import Post, Like, Comment


class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'created_at', 'status')
        list_filter = ('author', 'created_at', 'status')
        search_fields = ['title']
        ordering = ['-created_at']

class LikeAdmin(admin.ModelAdmin):
        list_display = ('user', 'post','created_at')
        list_filter = ('user', 'post')
        search_fields = ['user__name', 'post__title']
        ordering = ['-created_at']

class CommentAdmin(admin.ModelAdmin):
        list_display = ('user', 'post', 'content', 'created_at')
        list_filter = ('user', 'post')
        search_fields = ['content', 'user__name', 'post__title']
        ordering = ['-created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)