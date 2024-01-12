from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(null=True, max_length=1000)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("project-detail-page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} ({self.rating})"
