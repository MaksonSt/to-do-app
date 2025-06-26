from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    data_added = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


