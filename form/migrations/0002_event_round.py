# Generated by Django 4.2 on 2023-09-01 17:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('team_type', models.CharField(choices=[('team', 'Team'), ('solo', 'Solo'), ('both', 'Team/Solo')], max_length=4)),
                ('team_size', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('dept', models.CharField(choices=[('cse', 'Computer Science'), ('ece', 'ECE'), ('eee', 'EEE'), ('mech', 'Mechanical'), ('civil', 'Civil'), ('chem', 'Chemical'), ('it', 'Information Technology'), ('bme', 'Biomedical Engineering')], max_length=5)),
                ('rounds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('first_prize', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('second_prize', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('third_prize', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_rounds', to='form.event')),
            ],
        ),
    ]