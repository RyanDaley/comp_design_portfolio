from django.contrib import admin

from .models import Project, Author, Address
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Author)
admin.site.register(Address)