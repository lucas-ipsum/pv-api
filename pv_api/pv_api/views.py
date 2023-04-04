from rest_framework import viewsets
from .models import State
from .serializers import StateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['state']

    def get_queryset(self):
        queryset = State.objects.all()
        filter_backends = self.filter_queryset(queryset)

        serializer = StateSerializer(filter_backends)
        #return Response(serializer.data)
        print(type(serializer))
        #print(serializer['id'])
        return filter_backends  
       # return serializer
