from rest_framework import serializers
from .models import Repository
from Language.models import Language


class RepositorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    star = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.url.replace('api.', '').replace('repos/', '')

    def get_star(self, obj):
        return -obj.star

    def get_user(self, obj):
        return obj.url.replace('https://api.github.com/', '').replace('repos/', '').replace('/' + obj.name, '')

    class Meta:
        model = Repository
        fields = ['url', 'star', 'language', 'desc', 'name', 'user', 'created_at']
