import pytest
from tasks.models import Task
from datetime import date

# @pytest.mark.django_db allows DB access in your test.
@pytest.mark.django_db
def test_task_creation():
    task = Task.objects.create(title="Testing", due_date=date.today())
    assert task.id is not None
    assert task.title == "Testing"
