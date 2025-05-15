import pytest
from tasks.models import Task
from tasks.tasks import log_task_action
from datetime import date
import os

@pytest.mark.django_db
def test_log_task_action(tmp_path, settings):
    # Ensure log directory exists
    os.makedirs("logs", exist_ok=True)
    task = Task.objects.create(title="CeleryTest", due_date=date.today())
    log_task_action(task.id, "created")

    # Check the log file for correct entry
    with open("logs/task_activity.log") as f:
        log_lines = f.readlines()
        assert any("CeleryTest" in line for line in log_lines)