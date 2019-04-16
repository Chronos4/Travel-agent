from rest_framework import generics
from .serializers import AdventureListSerializer
from travel.models import Adventure


class AdventureListApi(generics.ListAPIView):
	serializer_class = AdventureListSerializer
	queryset = Adventure.objects.all()


