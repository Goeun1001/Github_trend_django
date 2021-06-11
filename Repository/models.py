from django.db import models
from Language.models import Language
from datetime import datetime


class Repository(models.Model):
    url = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, null=True, blank=True)
    star = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.name
