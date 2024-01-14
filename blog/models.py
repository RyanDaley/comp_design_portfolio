from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(null=True, max_length=1000)
    slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="projects")

    def get_absolute_url(self):
        return reverse("project-detail-page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
