from rest_framework import serializers
from .models import Topic
from django.db.models import Sum


class TopicSerializer(serializers.ModelSerializer):
    total_count = serializers.SerializerMethodField()

    def get_total_count(self, obj):
        total = Topic.objects.filter(language=obj.language).aggregate(Sum('count'))
        return total['count__sum']


    class Meta:
        model = Topic
        fields = ['name', 'language', 'count', 'total_count']
