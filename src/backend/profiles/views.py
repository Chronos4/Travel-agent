from django.shortcuts import render
from django.views.generic import DetailView
from .models import UserProfile
from django.http import Http404


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
