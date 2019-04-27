from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from .models import UserProfile
from django.http import Http404
from django.contrib.auth import get_user_model
from profiles.models import Contact


class UserProfileDetail(DetailView):
    template_name = 'profiles/user-profile.html'
    model = UserProfile

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = UserProfile.objects.get(user__slug=slug)
        except UserProfile.DoesNotExist:
            raise Http404('User does not exist')
        except UserProfile.MultipleObjectsReturned:
            qs = UserProfile.objects.filter(user__slug=slug)
            instance = qs.first()
        except:
            raise Http404('An error has occured')
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileDetail, self).get_context_data(
            *args, **kwargs)
        user = User.objects.filter(
            slug=self.kwargs.get('slug')).first()
        context['object'] = user
        profile = UserProfile.objects.get(user=user)
        context['profile'] = profile
        return context


User = get_user_model()


def UserFollow(request, slug):
    if request.user.is_authenticated:
        get_user = User.objects.filter(slug=slug)
        if get_user.exists():
            person = get_user.first()
            qs = Contact.objects.filter(user_from=request.user, user_to=person)
            if qs.exists():
                qs.first().delete()
            else:
                Contact.objects.create(
                    user_from=request.user, user_to=person)
            return render(request, 'profiles/user-profile.html', {'object': person})

    else:
        return redirect('login')
