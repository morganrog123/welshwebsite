# Generated by Django 2.0 on 2020-05-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welsh', '0009_lessonphrase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_phrase', models.CharField(default='', max_length=150)),
                ('current_translated_phrase', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='lessonphrase',
            name='phrase',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='lessonphrase',
            name='translated_phrase',
            field=models.CharField(default='', max_length=150),
        ),
    ]
