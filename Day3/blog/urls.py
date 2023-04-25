from django.urls import path
from .views import *

urlpatterns = [
    path(
        "posts/",
        PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post-list",
    ),
    path(
        "posts/<int:pk>/",
        PostViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="post-detail",
    ),
    path("posts/search/", PostViewSet.as_view({"get": "search"}), name="post-search"),
    path(
        "posts/<int:post_pk>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comment-list",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="comment-detail",
    ),
]
