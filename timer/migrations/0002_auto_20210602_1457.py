# Generated by Django 3.2.3 on 2021-06-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='intervals',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Interval',
        ),
    ]