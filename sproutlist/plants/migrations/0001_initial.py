# Generated by Django 5.0.2 on 2024-02-15 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('watering_interval', models.IntegerField(help_text='Days between watering')),
                ('last_watered', models.DateField(auto_now_add=True)),
                ('fertilization_interval', models.IntegerField(help_text='Days between fertilization')),
                ('last_fertilized', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('WATER', 'Water'), ('FERTILIZE', 'Fertilize')], max_length=20)),
                ('due_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
        ),
    ]