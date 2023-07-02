from django.shortcuts import render
from django.views import generic

from service.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("tags")
    paginate_by = 3


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5
