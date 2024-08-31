from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by("is_done", "-created_time")


class TagListView(generic.ListView):
    model = Tag
