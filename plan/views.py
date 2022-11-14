from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from plan.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    success_url = reverse_lazy("plan:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("plan:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("plan:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("plan:task-list")


class TagListView(generic.ListView):
    model = Tag
    success_url = reverse_lazy("plan:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("plan:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("plan:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("plan:tag-list")


def toggle_assign_to_tag(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("plan:task-list", args=[pk]))
