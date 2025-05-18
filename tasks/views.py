from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer

from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Welcome to TaskFlow API")


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer
