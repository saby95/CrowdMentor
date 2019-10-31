from django.db import models
from django.contrib.auth.models import User


class ResearchTasks(models.Model):
    AUDIT_SELECTION = (
        (1, 'Task'),
        (2, 'Worker')
    )
    task_type = models.CharField(max_length=10, blank = True, null=True)
    task_summary = models.CharField(max_length=500, default = 'Enter a single line summary')
    task_desc = models.TextField(default = 'Describe the task')
    creator_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    num_workers = models.PositiveIntegerField(default=1)
    audit_by = models.IntegerField(choices=AUDIT_SELECTION, default=2)
    audit_prob = models.DecimalField(max_digits=3, decimal_places=2, default=0.50)
    salary_by = models.IntegerField(choices=AUDIT_SELECTION, default=2)
    salary_task = models.DecimalField(max_digits=4, decimal_places=2, default=0.02)
    bonus_task = models.DecimalField(max_digits=4, decimal_places=2, default=0.01)
    fine_task = models.DecimalField(max_digits=4, decimal_places=2, default=0.01)


    def __str__(self):
        return self.task_summary
