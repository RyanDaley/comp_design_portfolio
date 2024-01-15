from django.shortcuts import render, get_object_or_404
from django.http import Http404
from datetime import date

from .models import Project



# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):
    latest_projects = projects = Project.objects.all().order_by("-date")[:3] #django creates one long SQL querry based on this line, better for performance
    num_projects = projects.count()
    return render(request, "blog/index.html", {
        "projects": latest_projects,
        "total_number_of_projects": num_projects
    })

def posts(request):
    all_posts = Project.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "blog/post-detail.html", {
        "project": project,
        "tags": project.tags.all()
    })