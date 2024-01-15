from django.contrib import admin

from .models import Project, Author, Tag
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Author)
admin.site.register(Tag)