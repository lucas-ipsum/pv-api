from rest_framework import viewsets
from .models import State
from .serializers import StateSerializer


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    print(serializer_class)
    print(queryset)

    def get_queryset(self):
        states = State.objects.all()
        return states  