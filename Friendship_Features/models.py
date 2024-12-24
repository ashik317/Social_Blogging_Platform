from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

'''
Friendship Features
○ Send Friend Requests: Users can send friend requests to other users.
○ Accept/Reject Requests: Users can accept or reject friend requests.
○ Friends List: Displays all accepted friends.
○ Visibility of Posts: Only friends can see and interact with each other’s posts
'''
class StatusChoices(models.TextChoices):
    SENT = 'sent', 'Sent'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'

class Friendship(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    friend = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_requests')
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.SENT)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.friend.email} {self.status}"

    def accept(self):
        self.status = StatusChoices.ACCEPTED
        self.save()

    def reject(self):
        self.status = StatusChoices.REJECTED
        self.save()

    def reverse_relationship(self):
        """ Returns the reverse friendship if exists """
        return Friendship.objects.get(user=self.friend, friend=self.user)

    class Meta:
        unique_together = ('user', 'friend')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendship_posts')

    def __str__(self):
        return self.title

    def is_visible(self, user):
        return (Friendship.objects.filter(
                    user=self.author,
                    friend=user,
                    status=StatusChoices.ACCEPTED
                ).exists() or self.author == user)

