from datetime import date
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_task(api_client):
    url = reverse("task-list")  # If you're using a DRF viewset with basename "task"
    data = {
            "title": "Test Task",
            "due_date": date.today(),
        }
    
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "Test Task"

@pytest.mark.django_db
def test_get_tasks(api_client):
    Task.objects.create(title="Task 1", due_date= date.today())
    Task.objects.create(title="Task 2", due_date= date.today())
    url = reverse("task-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
