# Generated by Django 2.0 on 2020-05-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20200528_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hangmangame',
            name='user',
        ),
        migrations.DeleteModel(
            name='HangmanGame',
        ),
    ]
