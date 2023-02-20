from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=200)
    desc = models.TextField()
    auth = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title