from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Adventure
from profiles.models import UserProfile
from django.contrib import messages
from django.db.models import Q
from actions.utils import create_action


class ListDestinationView(ListView):
    template_name = 'travel/List-destinations.html'

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q')
        if q is not None:
            lookups_For_Destinations = Q(
                country__icontains=q) | Q(town__icontains=q)
            lookups_For_Profile = Q(user__first_name__icontains=q)
            query_for_destinations = Adventure.objects.filter(
                lookups_For_Destinations, active=True).distinct()
            query_for_profiles = UserProfile.objects.filter(
                lookups_For_Profile).distinct()
            query = query_for_destinations or query_for_profiles
        else:
            query = Adventure.objects.filter(active=True)
        return query


class DetailDestinationView(DetailView):
    template_name = "travel/Detail-destination.html"
    model = Adventure

    def get_object(self, *args, **kwargs):
        request = self.request
        unique_id = self.kwargs.get('unique_id')

        try:
            instance = Adventure.objects.get(unique_id=unique_id)
            create_action(request.user, 'Viewed destination', instance)
        except Product.DoesNotExist:
            create_action(
                request.user, 'Searched destination but no found', instance)
            raise Http404('Trip did not found')
        except Product.MultipleObjectsReturned:
            qs = Adventure.objects.filter(unique_id=unique_id)
            instance = qs.first()
        except:
            raise Http404('An error has occured')
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(DetailDestinationView,
                        self).get_context_data(*args, **kwargs)
        query = self.object.users.all().exclude(
            email=self.object.author.email)
        context['users'] = query
        return context


def AdventureJoin(request, unique_id):
    if request.user.is_authenticated:
        query = Adventure.objects.filter(unique_id=unique_id)
        if query.exists():
            obj = query.first()
            if request.user != obj.author:
                filt = obj.users.all()
                if request.user not in filt:
                    obj.users.add(request.user)
                    create_action(request.user, 'Enrolled In Destination', obj)
                    messages.success(request, 'You successfully enrolled')
                elif request.user in filt:
                    messages.warning(
                        request, 'You successfully canceled the registration')
                    create_action(
                        request.user, 'Removed From Destination', obj)
                    obj.users.remove(request.user)
    else:
        return redirect('login')
    return redirect('travel:destination-detail', unique_id=unique_id)


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
                    create_action(self.request.user,
                                  'Deleted Destination', adv)
                    adv.active = False
                    adv.save()
                    messages.success(
                        self.request, 'You deleted the post successfully!')
                    return redirect('travel:destination-list')
                else:
                    print('error my friend')
                    messages.error(
                        self.request, 'You are not the author of this post to delete it!')
                    unique_id = self.kwargs['unique_id']
                    return redirect('travel:destination-detail', unique_id=self.kwargs.get('unique_id'))
