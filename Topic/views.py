from rest_framework import viewsets
from .models import Topic
from .serializers import TopicSerializer
from github.pagination import ScrollPagination


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all().order_by('-count')
    pagination_class = ScrollPagination


topic_list = TopicViewSet.as_view({
    'get': 'list',
})


class TopicDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    pagination_class = ScrollPagination

    def get_queryset(self):
        query = self.request.GET['q']
        queryset = Topic.objects.filter(language__language=query[0].upper() + query[1:]).order_by('-count')
        return queryset


topic_detail = TopicDetailViewSet.as_view({
    'get': 'list',
})