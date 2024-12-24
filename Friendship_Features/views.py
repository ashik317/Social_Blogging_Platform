from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Friendship_Features.models import Friendship, Post, StatusChoices
from .forms import PostForm
from django.db.models import Q

@login_required
def send_friend_request(request):
    User = get_user_model()
    users = User.objects.exclude(pk=request.user.pk)  # Exclude the logged-in user

    if request.method == 'POST':
        friend_id = request.POST.get('friend')
        friend = get_object_or_404(User, pk=friend_id)

        if request.user == friend:
            return render(request, 'Friendship_Features/error.html',
                          {'message': 'You cannot send a friend request to yourself.'})

        friendship, created = Friendship.objects.get_or_create(
            user=request.user, friend=friend, defaults={'status': StatusChoices.SENT}
        )

        if created:
            return redirect('Friendship_Features:friend_list')

        return render(request, 'Friendship_Features/error.html', {'message': 'Friend request already sent.'})

    return render(request, 'Friendship_Features/send_friend_request.html', {'users': users})

@login_required
def accept_friend_request(request, request_id):
    friendship = get_object_or_404(Friendship, pk=request_id, friend=request.user)
    friendship.status = StatusChoices.ACCEPTED
    friendship.save()
    return redirect('Friendship_Features:friend_list')

@login_required
def reject_friend_request(request, request_id):
    friendship = get_object_or_404(Friendship, pk=request_id, friend=request.user)
    friendship.status = StatusChoices.REJECTED
    friendship.save()
    return redirect('Friendship_Features:friend_list')

@login_required
def friend_list(request):
    friends = Friendship.objects.all()
    return render(request, 'Friendship_Features/friend_list.html', {'friends': friends})


@login_required
def friend_requests_list(request):
    requests = Friendship.objects.all()
    return render(request, 'Friendship_Features/friend_requests_list.html', {'requests': requests})

@login_required
def post_list(request):
    friends = Friendship.objects.all()
    return render(request, 'Friendship_Features/post_list.html', {'friends': friends})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Friendship_Features:post_list')
    else:
        form = PostForm()
    return render(request, 'Friendship_Features/create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    if not post.is_visible(request.user):
        return render(request, 'Friendship_Features/error.html', {'message': 'You do not have permission to view this post.'})
    return render(request, 'Friendship_Features/post_detail.html', {'post': post})
