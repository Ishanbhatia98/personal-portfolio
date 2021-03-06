# Generated by Django 2.2.2 on 2020-05-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='grade',
        ),
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='duration',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='summary',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
