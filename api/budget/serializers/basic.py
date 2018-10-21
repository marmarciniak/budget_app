from budget.models import Budget
from rest_framework import serializers


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('start_date', 'end_date', 'budget')

