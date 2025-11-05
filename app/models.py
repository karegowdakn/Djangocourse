from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import re

from .managers import UserProfileManager


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def article_count(self):
        return self.articles.count()
    
    @property
    def written_words(self):
        return self.articles.aggregate(models.Sum("word_count"))["word_count__sum"] or 0


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default=0)
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20, 
        default="draft", 
        choices=[
            ("draft", "Draft"),
            ("published", "Published"),
            ("in_progress", "In Progress"),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    # this one will automatically update the word count into db
    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", '', self.content).replace('&nbsp;', ' ')
        self.word_count = len(re.findall(r'\b\w+\b', text))
        # self.word_count = len(self.content.split())
        super().save(*args, **kwargs)