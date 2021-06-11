from django.db import models
from Language.models import Language


class Topic(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    count = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
