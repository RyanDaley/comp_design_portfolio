from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
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

class SinglePostView(View):
    def is_stored_post(self, request, project_id):
        stored_projects = request.session.get("stored_projects")
        if stored_projects is not None:
            is_saved_for_later = project_id in stored_projects
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        
        context = {
            "project": project,
            "tags": project.tags.all(),
            "comment_form": CommentForm(),
            "comments":project.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, project.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        project = Project.objects.get(slug=slug)

        if(comment_form.is_valid()):
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        
        context = {
            "project": project,
            "tags": project.tags.all(),
            "comment_form": CommentForm(),
            "comments":project.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

# def project_detail(request, slug):
#     project = get_object_or_404(Project, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "project": project,
#         "tags": project.tags.all()
#     })
    
class ReadLaterView(View):
    def get(self, request):
        stored_projects = request.session.get("stored_projects")

        context = {}

        if stored_projects is None or len(stored_projects) == 0:
            context["projects"] = []
            context["has_projects"] = False
        else:
            projects = Project.objects.filter(id__in=stored_projects)
            context["projects"] = projects
            context["has_projects"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_projects = request.session.get("stored_projects")

        if stored_projects is None:
            stored_projects = []
        
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_projects:
            stored_projects.append(post_id)
            request.session["stored_projects"] = stored_projects
        else: 
            stored_projects.remove(post_id)

        
        return HttpResponseRedirect("/")