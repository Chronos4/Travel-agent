from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Adventure


class ListDestinationView(ListView):
    template_name = 'travel/List-destinations.html'

    def get_queryset(self, *args, **kwarg):
        return Adventure.objects.filter(active=True)


class DetailDestinationView(DetailView):
    template_name = "travel/Detail-destination.html"
    model = Adventure

    def get_object(self, *args, **kwargs):
        request = self.request
        unique_id = self.kwargs.get('unique_id')

        try:
            instance = Adventure.objects.get(unique_id=unique_id)
        except Product.DoesNotExist:
            raise Http404('Product did not found')
        except Product.MultipleObjectsReturned:
            qs = Products.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404('An error has occured')
        return instance
