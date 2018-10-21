from budget.models import *
from rest_framework import viewsets
from .serializers.basic import *


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Budget.objects.all().order_by('-start_date')
    serializer_class = BudgetSerializer

