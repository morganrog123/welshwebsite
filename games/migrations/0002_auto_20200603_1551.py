# Generated by Django 2.0 on 2020-06-03 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
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
