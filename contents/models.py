from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    youtube_id = models.CharField(max_length=20, blank=True)
    instagram_id = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "게시물"
        verbose_name_plural = "게시물들"

    def __str__(self):
        return self.title
