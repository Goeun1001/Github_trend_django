from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=100, primary_key=True)
    count = models.IntegerField()

    def __str__(self):
        return self.language