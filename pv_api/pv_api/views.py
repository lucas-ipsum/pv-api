from rest_framework import viewsets
from .models import State
from .serializers import StateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state']
    print(filterset_fields)
    print('hi')

    def get_queryset(self):
        states = State.objects.all()
        return states  
