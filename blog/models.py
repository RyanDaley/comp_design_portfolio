from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(default = "", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



class Project(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200, default = "")
    image_name = models.CharField(max_length=100, default = "")
    date = models.DateField(auto_now=True)
    content = models.TextField(default = "")
    slug = models.SlugField(default="", blank=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="projects")
    tags = models.ManyToManyField(Tag)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
