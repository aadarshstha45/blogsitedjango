from django.db import models
from user.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStamp):
    title = models.CharField(max_length=255)
    body = models.TextField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )


def __str__(self):
    return self.title
