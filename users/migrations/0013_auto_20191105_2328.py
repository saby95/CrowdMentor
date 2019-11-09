# Generated by Django 2.2.6 on 2019-11-05 23:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191031_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sam',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tu',
            name='user',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='audit_prob_user',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0299999999999999988897769753748434595763683319091796875'), max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='claimed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='completed_audits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='completed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0200000000000000004163336342344337026588618755340576171875'), max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_Mentor',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='mentees',
            field=models.CharField(default='[]', max_length=10000),
        ),
        migrations.AddField(
            model_name='profile',
            name='mentors',
            field=models.CharField(default='[]', max_length=10000),
        ),
        migrations.AddField(
            model_name='profile',
            name='open_audits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='open_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='performance',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.05000000000000000277555756156289135105907917022705078125'), max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_audits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_posted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_salary',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='worker_pool',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('task_updater', 'task_updater'), ('auditor', 'auditor'), ('worker', 'worker')], default='worker', max_length=15),
        ),
        migrations.DeleteModel(
            name='Auditor',
        ),
        migrations.DeleteModel(
            name='Sam',
        ),
        migrations.DeleteModel(
            name='Tu',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]