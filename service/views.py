from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from service.forms import TaskForm
from service.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 3


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("service:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("service:task-list")


class TaskCompleteUpdateView(generic.UpdateView):
    model = Task
    fields = ["mark"]
    success_url = reverse_lazy("service:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("service:task-delete")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("service:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("service:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("service:tag-list")
