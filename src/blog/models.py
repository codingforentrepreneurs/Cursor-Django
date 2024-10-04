from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    is_published = models.BooleanField('ready to publish', default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.pub_date:
            self.pub_date = timezone.now()
        super().save(*args, **kwargs)
