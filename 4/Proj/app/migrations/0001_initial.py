# Generated by Django 5.2.1 on 2025-05-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursecode', models.CharField(max_length=10)),
                ('coursename', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('sem', models.IntegerField()),
                ('enrollment', models.ManyToManyField(related_name='students', to='app.course')),
            ],
        ),
    ]
