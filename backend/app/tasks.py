from celery import shared_task
from .jobs import Job

@shared_task
def import_jobs_task():
    """Background task to import jobs"""
    Job.fetch_and_store_jobs()
