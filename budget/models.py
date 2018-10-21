from django.db import models
from datetime import date


class Budget(models.Model):
    start_date = models.DateField(default=date.today())
    end_date = models.DateField(default=date.today())
    budget = models.DecimalField(max_digits=11, decimal_places=2)

class PlannedExpenses(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    cause = models.CharField(max_length=100)

class Spendings(models.Model):
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    cause = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    planned = models.ForeignKey(PlannedExpenses, on_delete=models.CASCADE)



