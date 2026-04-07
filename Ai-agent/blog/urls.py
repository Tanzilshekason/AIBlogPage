from django.urls import path
from .views import (
    RegisterView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like_post,
    add_comment,
    profile_view,
    toggle_follow
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('user/<str:username>/', profile_view, name='profile'),
    path('user/<str:username>/follow/', toggle_follow, name='toggle_follow'),
]
