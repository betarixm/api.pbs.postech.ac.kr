from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    youtube_id = models.CharField(max_length=20, blank=True)
    instagram_id = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "게시물"
        verbose_name_plural = "게시물들"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)


class Sequence(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    articles = models.ManyToManyField(Article)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
