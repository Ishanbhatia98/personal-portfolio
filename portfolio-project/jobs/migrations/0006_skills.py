# Generated by Django 2.2.2 on 2020-05-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200512_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_title', models.CharField(default='default', max_length=100)),
                ('ts_summary', models.CharField(default='default', max_length=300)),
                ('s_title', models.CharField(default='default', max_length=100)),
            ],
        ),
    ]
