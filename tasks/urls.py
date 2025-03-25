from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTasksView

urlpatterns = [
    path("tasks/create/", TaskCreateView.as_view(), name="create-task"),
    path("tasks/assign/<int:task_id>/", TaskAssignView.as_view(), name="assign-task"),
    path("tasks/user/<int:user_id>/", UserTasksView.as_view(), name="user-tasks"),
]