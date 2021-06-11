from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
from github.pagination import ScrollPagination
from Repository.models import Repository
from Repository.serializers import RepositorySerializer


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all().order_by('-count')
    pagination_class = ScrollPagination


language_list = LanguageViewSet.as_view({
    'get': 'list',
})



class LanguageSearchViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    pagination_class = ScrollPagination

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = Language.objects.filter(language__startswith=query)
        return queryset


language_search = LanguageSearchViewSet.as_view({
    'get': 'list',
})


class LanguageRepoViewSet(viewsets.ModelViewSet):
    serializer_class = RepositorySerializer
    pagination_class = ScrollPagination

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = Repository.objects.filter(language__language=query[0].upper() + query[1:]).order_by('star')
        return queryset


language_repo = LanguageRepoViewSet.as_view({
    'get': 'list',
})
