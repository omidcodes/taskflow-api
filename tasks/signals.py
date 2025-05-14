from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task
from tasks.tasks import log_task_action


@receiver(post_save, sender=Task)
def task_created_handler(sender, instance, created, **kwargs):
    if created:
        log_task_action.delay(instance.id, "created")
