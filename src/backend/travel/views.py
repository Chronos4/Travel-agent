from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Adventure
from django.contrib import messages


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
            raise Http404('Trip did not found')
        except Product.MultipleObjectsReturned:
            qs = Adventure.objects.filter(unique_id=unique_id)
            instance = qs.first()
        except:
            raise Http404('An error has occured')
        return instance


def AdventureJoin(request, unique_id):
    if request.user.is_authenticated:
        query = Adventure.objects.filter(unique_id=unique_id)
        if query.exists():
            obj = query.first()
            if request.user != obj.author:
                filt = obj.users.all()
                if request.user not in filt:
                    obj.users.add(request.user)
                    messages.success(request, 'You successfully enrolled')
                elif request.user in filt:
                    messages.info(
                        request, 'You successfully canceled the registration')
                    obj.users.remove(request.user)
    else:
        return redirect('login')
    return redirect('destination-detail', unique_id=unique_id)


class DeleteDestinationView(DeleteView):
    model = Adventure
    template_name = 'travel/Delete-destination.html'
    success_url = 'travel/List-destinations.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            query = Adventure.objects.filter(
                unique_id=self.kwargs.get('unique_id')) or None
            if query.exists():
                adv = query.first()
                if self.request.user == adv.author:
                    adv.delete()
                    messages.success(
                        self.request, 'You deleted the post successfully!')
                    return redirect('destination-list')
                else:
                    print('error my friend')
                    messages.error(
                        self.request, 'You are not the author of this post to delete it!')
                    unique_id = self.kwargs['unique_id']
                    return redirect('destination-detail', unique_id=self.kwargs.get('unique_id'))
