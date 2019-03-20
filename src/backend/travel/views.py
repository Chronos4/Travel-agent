from django.shortcuts import render
from django.views.generic import ListView
from .models import Adventure


class ListDestinationView(ListView):
    template_name = 'travel/List-destinations.html'

    def get_queryset(self, *args, **kwarg):
        return Adventure.objects.filter(active=True)
    

