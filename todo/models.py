from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=69)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return f"{self.content} - {self.is_done}"
