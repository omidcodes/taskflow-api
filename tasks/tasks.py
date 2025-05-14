from celery import shared_task
from django.utils.timezone import now
from tasks.models import Task

@shared_task
def log_task_action(task_id, action):
    """Log task ID and title to a file."""
    try:
        task = Task.objects.get(id=task_id)
        log_line = f"[{now()}] Logging Celery Task : Task #{task.id} ('{task.title}') was {action} using celery.\n"
    except Task.DoesNotExist:
        log_line = f"[{now()}] ERROR: Task {task_id} not found for action '{action}'\n"

    with open("logs/task_activity.log", "a") as f:
        f.write(log_line)
