# Generated by Django 2.1.2 on 2018-10-21 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plannedexpenses',
            name='budget',
        ),
        migrations.AlterField(
            model_name='spendings',
            name='planned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.PlannedExpenses'),
        ),
    ]
