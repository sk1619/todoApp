from django.db import models

# Create your models here.


class States(models.Model):

    states = models.CharField(max_length=100)

    class Meta:
        db_table = 'states'

    def __str__(self):
        return self.states


class TaskList(models.Model):
    id = models.AutoField(primary_key=True)
    tasks = models.CharField(max_length=1000)
    due_date = models.DateField(null=False)  # 2010-01-15 - Default input Format
    task_state = models.ForeignKey(States, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasklist'

    def __str__(self):
        return self.tasks



