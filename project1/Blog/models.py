from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(null=False, max_length=255, default="")
    text = models.CharField(null=False, max_length=3000, default="")
    author = models.CharField(null=False, max_length=255, default="Taubay")

    def __str__(self):
        return f"ID of BLog: {self.id}, Title:{self.title}"
