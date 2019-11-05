from django.forms import ModelForm
from .models import ResearchTasks, TaskUserJunction, Audit

class AddTaskForm(ModelForm):
    class Meta:
        model = ResearchTasks
        fields = ['task_summary', 'task_desc', 'num_workers', 'audit_by', 'audit_prob', 'salary_by', 'salary_task', 'bonus_task', 'fine_task']



class AnswerForm(ModelForm):
    class Meta:
        model = TaskUserJunction
        fields = ['answer', 'comment', 'confidence_level']

class AuditForm(ModelForm):
    class Meta:
        model = Audit
        fields = ['task_correct', 'review']
