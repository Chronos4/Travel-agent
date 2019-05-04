from rest_framework import generics
from .serializers import AdventureListSerializer
from travel.models import Adventure


class AdventureListApi(generics.ListAPIView):
    serializer_class = AdventureListSerializer
    queryset = Adventure.objects.all()


class AdventureRetrieveApi(generics.RetrieveAPIView):
    serializer_class = AdventureListSerializer
    queryset = Adventure.objects.filter(active=True)
    lookup_field = 'unique_id'
