from django.contrib import admin
from Friendship_Features.models import Friendship,Post

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('friend','user', 'status', 'blocked')
    list_filter = ('status', 'blocked')
    search_fields = ('user__name','friend__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')
    list_filter = ('content',)
    search_fields = ('title', 'author__username')

