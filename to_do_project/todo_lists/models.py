from django.db import models
from django.conf import settings


class ListOfTasks(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def success_percentage(self):
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        tasks_complete = self.tasks.filter(complete=True).count()
        return round((tasks_complete / total_tasks) * 100, 1)


    def __str__(self):
        return self.name
