# Generated by Django 4.2 on 2023-04-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a pre-workout name', max_length=200)),
                ('brand', models.CharField(default=' ', max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bcaainstance',
            name='Bcaa',
        ),
        migrations.RemoveField(
            model_name='bcaainstance',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='creatineinstance',
            name='Creatine',
        ),
        migrations.RemoveField(
            model_name='creatineinstance',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='preworkoutinstance',
            name='PreWorkout',
        ),
        migrations.RemoveField(
            model_name='preworkoutinstance',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='proteininstance',
            name='Protein',
        ),
        migrations.RemoveField(
            model_name='proteininstance',
            name='inventory',
        ),
        migrations.DeleteModel(
            name='Bcaa',
        ),
        migrations.DeleteModel(
            name='BcaaInstance',
        ),
        migrations.DeleteModel(
            name='Creatine',
        ),
        migrations.DeleteModel(
            name='CreatineInstance',
        ),
        migrations.DeleteModel(
            name='PreWorkout',
        ),
        migrations.DeleteModel(
            name='PreWorkoutInstance',
        ),
        migrations.DeleteModel(
            name='Protein',
        ),
        migrations.DeleteModel(
            name='ProteinInstance',
        ),
    ]
