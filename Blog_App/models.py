from django.conf import settings
from django.db import models
'''
Blog Posts
○ Create Post: Users can create, edit, and delete their blog posts.
○ View Posts: Users can view their own posts and posts of friends.
○ Like Posts: Users can like posts to show appreciation.
○ Comments: Users can comment on their own or friends’ blog posts.
'''
class StatusChoices(models.TextChoices):
    Draft = 'Draft', 'Draft'
    Published = 'Published', 'Published'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.Draft)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked '{self.post.title}'"

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Comment ON '{self.post.title}'"
