# Django core
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.http import Http404
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# my apps
from .models import Adventure, Destination_comment
from .forms import Comment_Form, Create_form
from profiles.models import UserProfile
from actions.utils import create_action


class ListDestinationView(ListView):
    template_name = 'travel/list-destinations.html'

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q')
        if q is not None:
            lookups_For_Destinations = Q(
                country__icontains=q) | Q(town__icontains=q)
            query_for_destinations = Adventure.objects.filter(
                lookups_For_Destinations, active=True).distinct()
            query = query_for_destinations
            if(self.request.user.is_authenticated):
                create_action(self.request.user, f'Searched for --> {q}')
        else:
            query = Adventure.objects.filter(active=True)
        return query

    def get_context_data(self, *args, **kwargs):
        """ Display destinations about request user preference """
        context = super(ListDestinationView,
                        self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            profile = UserProfile.objects.get(user=self.request.user)
            if profile:
                if profile.places_to is not None:
                    places_want_to_travel = profile.places_to.split(",")
                    destinations = Adventure.objects.filter(
                        town__in=places_want_to_travel, active=True)
                    context["preferred_destinations"] = destinations
        return context


class DetailDestinationView(FormMixin, DetailView):
    template_name = "travel/detail-destination.html"
    model = Adventure
    form_class = Comment_Form

    def get_object(self, *args, **kwargs):
        request = self.request
        unique_id = self.kwargs.get('unique_id')
        try:
            instance = Adventure.objects.get(unique_id=unique_id)
            if request.user.is_authenticated:
                create_action(request.user, 'Viewed destination', instance)
        except Adventure.DoesNotExist:
            create_action(
                request.user, 'Searched destination but no found', instance)
            raise Http404('Trip did not found')
        except Adventure.MultipleObjectsReturned:
            qs = Adventure.objects.filter(unique_id=unique_id)
            instance = qs.first()
        except:
            raise Http404('An error has occured')
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(DetailDestinationView,
                        self).get_context_data(*args, **kwargs)
        query = self.object.users.all()
        # get all the comments related to this post
        comments_list = self.object.comments.all()
        # add a paginator
        paginator = Paginator(comments_list, 5)
        page = self.request.GET.get('page')
        comments = paginator.get_page(page)
        context['users'] = query
        context['form'] = self.form_class
        context['comments'] = comments
        return context

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                destination = self.get_object()
                new_comment = form.save(commit=False)
                new_comment.post = destination
                new_comment.user = self.request.user
                new_comment.save()
                return self.form_valid(new_comment)
            else:
                return self.form_invalid(new_comment)
        else:
            return redirect('login')

    def get_success_url(self):
        if self.request.method == "POST":
            return reverse('travel:destination-detail', kwargs={'unique_id': self.kwargs.get('unique_id')})


def AdventureJoin(request, unique_id):
    if request.user.is_authenticated:
        joined = Adventure.objects.join(request, unique_id)
        if joined:
            messages.success(request, 'You successfully enrolled')
        else:
            messages.warning(
                request, 'You successfully canceled the registration')
    else:
        return redirect('login')
    return redirect('travel:destination-detail', unique_id=unique_id)


def create_destination_view(request):
    if request.user.is_authenticated:
        form = Create_form()
        if request.method == "POST":
            form = Create_form(request.POST or None, request.FILES or None)
            if form.is_valid():
                # get the instance that the form created
                instance = form.instance
                instance.author = request.user
                instance.save()
                create_action(request.user, "Created new trip", instance)
                instance.users.add(request.user)
                return redirect('travel:destination-detail', unique_id=instance.unique_id)
            else:
                form = Create_form()
        return render(request, "travel/create-destination.html", {'form': form})
    return redirect('travel:destination-list')


def delete_destination_view(request, unique_id):
    if request.user.is_authenticated:
        query = Adventure.objects.filter(unique_id=unique_id)
        if query.count() == 1:
            trip = query.first()
            if request.user == trip.author:
                trip.active = False
                trip.save()
                create_action(request.user,
                              'Deleted Destination', trip)
                messages.success(request, "Trip successfully deleted")
                return redirect("travel:destination-list")
    return render(request, "travel/list-destination.html")
