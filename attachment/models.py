from django.db import models
from tasks.models import Task

# Create your models here.
class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_attachments/')
    description = models.TextField(blank=True)
