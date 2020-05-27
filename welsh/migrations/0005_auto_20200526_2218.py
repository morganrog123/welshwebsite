# Generated by Django 2.0 on 2020-05-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welsh', '0004_auto_20200526_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testtaker',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testtaker',
            name='user',
        ),
        migrations.AddField(
            model_name='test',
            name='answer',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='test',
            name='question',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='TestTaker',
        ),
    ]
