from django.db import models

# User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    TASK_STATUS = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default="pending")
    task_type = models.CharField(max_length=50, blank=True, null=True)
    assigned_users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return self.name