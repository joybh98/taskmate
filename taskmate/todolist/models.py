from django.db import models

# Create your models here.

class TaskList(models.Model):
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

    # return only the task name instead of TaskList <object>
    def __str__(self):
        return self.task + " - " + str(self.done)