from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=69)


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)
