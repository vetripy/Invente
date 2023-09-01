# Generated by Django 4.2 on 2023-09-01 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_event_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='first_prize',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='rounds',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='second_prize',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='team_size',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='third_prize',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]