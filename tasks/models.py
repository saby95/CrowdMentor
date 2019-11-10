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


class Audit(models.Model):
    YES_NO_CHOICES = (
        (None, ''),
        (True, 'Yes'),
        (False, 'No')
    )
    task_id = models.ForeignKey(ResearchTasks, on_delete=models.DO_NOTHING)
    auditor_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    task_correct = models.NullBooleanField(choices=YES_NO_CHOICES, max_length=3, blank=True, null=True, default=None,)
    review = models.TextField(default = 'Review')
    creation_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.task_id.task_summary


class TaskUserJunction(models.Model):
    CONFIDENCE = (
        (1, 'poor'),
        (2, 'below average'),
        (3, 'average'),
        (4, 'above average'),
        (5, 'good')
    )
    task_id = models.ForeignKey(ResearchTasks, on_delete=models.DO_NOTHING)
    room_id = models.IntegerField(default=0)
    worker_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    claim_time = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=500, null=True)
    submission_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    confidence_level = models.IntegerField(choices=CONFIDENCE, blank=True, null=True)
    task_audit = models.BooleanField(default=False)
    audit_id = models.ForeignKey(Audit, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.task_id.task_summary

