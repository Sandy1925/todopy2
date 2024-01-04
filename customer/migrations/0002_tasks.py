# Generated by Django 3.2.16 on 2023-12-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.IntegerField(max_length=2)),
                ('addedOn', models.DateField()),
                ('completedOn', models.DateField()),
                ('removedOn', models.DateField()),
            ],
        ),
    ]
