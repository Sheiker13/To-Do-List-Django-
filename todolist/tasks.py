from celery import shared_task
from .models import Task

@shared_task
def mark_completed_tasks():
    Task.objects.filter(completed=False).update(completed=True)
    return "All tasks marked as completed."
