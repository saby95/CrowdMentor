# Generated by Django 2.2.6 on 2019-10-30 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191030_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='claimed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workers',
            name='completed_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workers',
            name='open_tasks',
            field=models.IntegerField(default=0),
        ),
    ]
