from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from enum import Enum
import json

from django.dispatch import receiver
from django.db.models.signals import post_save



TRUE_OR_FALSE = [(True,'Yes'), (False,'No')]
pool_choices = [('A','A'),('B','B')]



class UserRoles(Enum):
    ADMIN = 'admin'
    TASK_UPDATER = 'task_updater'
    AUDITOR = 'auditor'
    WORKER = 'worker'


class Profile(models.Model):
    class Meta:
        app_label = 'users'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=[(tag.value, tag.value) for tag in UserRoles],
                            default=UserRoles.WORKER.value)
    performance = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.00))
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.05))
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.03))
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.02))
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00))
    audit_prob_user = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal(0.00))
    total_posted = models.IntegerField(default=0)
    open_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    claimed_tasks = models.IntegerField(default=0)
    total_audits = models.IntegerField(default=0)
    open_audits = models.IntegerField(default=0)
    completed_audits = models.IntegerField(default=0)
    is_Mentor = models.BooleanField(choices=TRUE_OR_FALSE,default=False)
    mentees = models.CharField(max_length=10000,default='[]')
    worker_pool = models.CharField(max_length=1,choices=pool_choices, default='A')
    mentors = models.CharField(max_length=10000,default='[]')

    def set_mentors(self, mentor_list):
        if not mentor_list:
            self.mentors = json.dumps([])
        else:
            self.mentors = json.dumps(mentor_list)

    def get_mentors(self):
        return json.loads(self.mentors)

    def set_mentees(self, mentees_list):
        if not mentees_list:
            self.mentees = json.dumps([])
        else:
            self.mentees = json.dumps(mentees_list)

    def get_mentees(self):
        return json.loads(self.mentees)


class Mentor(models.Model):
    class Meta:
        app_label = 'users'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


########    Services      ######


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

    if instance.username == 'admin':
        instance.profile.role = UserRoles.ADMIN.value
        instance.profile.save()


