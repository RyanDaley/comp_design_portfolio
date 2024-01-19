from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from datetime import date

from .models import Project
from .forms import CommentForm



# Create your views here.
def get_date(post):
    return post['date']

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Project
    ordering = ["-date"]
    context_object_name = "projects"

    def get_queryset(self):
        queryset= super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(request):
#     latest_projects = projects = Project.objects.all().order_by("-date")[:3] #django creates one long SQL querry based on this line, better for performance
#     num_projects = projects.count()
#     return render(request, "blog/index.html", {
#         "projects": latest_projects,
#         "total_number_of_projects": num_projects
#     })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Project
    ordering = ["-date"]
    context_object_name = "all_posts"  

# def posts(request):
#     all_posts = Project.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


# def project_detail(request, slug):
#     project = get_object_or_404(Project, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "project": project,
#         "tags": project.tags.all()
#     })