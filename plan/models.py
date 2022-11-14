from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    creation = models.DateTimeField()
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-creation"]

    def __str__(self):
        return f"{self.content} ({self.creation})"
