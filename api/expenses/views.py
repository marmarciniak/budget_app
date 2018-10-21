from budget.models import *
from rest_framework import viewsets
from .serializers.basic import ExpensesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PlannedExpenses.objects.all()
    serializer_class = ExpensesSerializer
