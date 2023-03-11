from django.db import models

# Create your models here.
class Github(models.Model):
    repo_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    html_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    html_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    html_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name