import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import date

@pytest.mark.django_db
def test_create_task_api():
    client = APIClient()
    url = reverse("task-list")  # Adjust if you use a different route name
    response = client.post(url, {
        "title": "API Task",
        "due_date": date.today(),
    }, format="json")
    assert response.status_code == 201
    assert response.data["title"] == "API Task"
