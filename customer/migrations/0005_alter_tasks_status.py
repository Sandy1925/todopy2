# Generated by Django 3.2.16 on 2024-01-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_tasks_removedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.IntegerField(),
        ),
    ]
