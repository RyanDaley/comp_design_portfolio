from django.shortcuts import render, get_object_or_404
from django.http import Http404
from datetime import date

from .models import Project



# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):
    projects = Project.objects.all().order_by("title")
    num_projects = projects.count()
    return render(request, "blog/index.html", {
        "projects": projects,
        "total_number_of_projects": num_projects
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": Project.objects.all()
    })

def project_detail(request, slug):
    # try:
    #     project = Project.objects.get(pk=id)
    # except:
    #     raise Http404()
    project = get_object_or_404(Project, slug=slug)
    return render(request, "blog/post-detail.html", {
        "project": project
    })