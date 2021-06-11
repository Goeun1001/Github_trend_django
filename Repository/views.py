from rest_framework import viewsets
from .models import Repository
from .serializers import RepositorySerializer
from github.pagination import ScrollPagination


class RepositoryViewSet(viewsets.ModelViewSet):
    serializer_class = RepositorySerializer
    queryset = Repository.objects.all().order_by('star')
    pagination_class = ScrollPagination


repo_list = RepositoryViewSet.as_view({
    'get': 'list',
})


class LatestRepositoryViewSet(viewsets.ModelViewSet):
    serializer_class = RepositorySerializer
    queryset = Repository.objects.all().order_by('-created_at')
    pagination_class = ScrollPagination


latest_repo_list = LatestRepositoryViewSet.as_view({
    'get': 'list',
})