from rest_framework import serializers
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "mobile"]


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Task
        fields = ["id", "name", "description", "created_at", "completed_at", "status", "task_type", "assigned_users"]


class TaskCreateSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ["name", "description", "task_type", "assigned_users"]
