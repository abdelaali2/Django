from .models import Post, Comment
from rest_framework import viewsets, filters
from rest_framework.filters import DateFilterBackend
from rest_framework.versioning import NamespaceVersioning
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PostPagination(PageNumberPagination):
    page_size = 5


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DateFilterBackend, filters.SearchFilter]
    filterset_fields = ["date_published"]
    search_fields = ["title"]
    pagination_class = PostPagination
    versioning_class = NamespaceVersioning


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Comment.objects.filter(post=post_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
