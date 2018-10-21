from budget.models import *
from rest_framework import viewsets





class SpendingsViewSet(viewsets.ModelViewSet):
    queryset = Spendings.objects.all()
    serializer_class = GroupSerializer

