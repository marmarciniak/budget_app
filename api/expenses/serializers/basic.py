from budget.models import PlannedExpenses
from rest_framework import serializers


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedExpenses
        fields = ('amount', 'cause')

