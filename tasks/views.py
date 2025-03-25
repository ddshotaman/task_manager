from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer


# API to Create a Task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


# API to Assign a Task to Users
class TaskAssignView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            user_ids = request.data.get("user_ids", [])
            users = User.objects.filter(id__in=user_ids)

            task.assigned_users.add(*users)
            task.save()

            return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


# API to Get Tasks Assigned to a Specific User
class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Task.objects.filter(assigned_users__id=user_id)
