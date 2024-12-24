from django.urls import path
from . import views

app_name = 'Friendship_Features'

urlpatterns = [
    path('friend_list/', views.friend_list, name='friend_list'),
    path('friend-send_friend_request/<int:friend_id>/', views.send_friend_request, name='send_friend_request'),
    path('friend-request/accept/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('friend-request/reject/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('friend-requests/', views.friend_requests_list, name='friend_requests_list'),
    path('post_list/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
]
