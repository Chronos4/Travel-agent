from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views import View
from .models import UserProfile
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth import get_user_model
from profiles.models import Contact
from actions.utils import create_action
from .forms import ProfileForm, PhotoUploadForm


class UserProfileDetail(DetailView):
    template_name = 'profiles/user-profile.html'
    model = UserProfile

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = UserProfile.objects.get(user__slug=slug)
            create_action(request.user, 'Viewed Profile', instance)
            return instance
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
        context['user'] = user
        profile = UserProfile.objects.get(user=user)
        context['profile'] = profile
        return context


User = get_user_model()


class UserFollow(View):

    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            request = self.request
            if request.user.is_authenticated:
                slug = self.kwargs.get('slug')
                get_user = User.objects.filter(slug=slug)
                if get_user.exists():
                    person = get_user.first()
                    if request.user == person:
                        return redirect('profiles:user-profile', slug=slug)
                    else:
                        qs = Contact.objects.filter(
                            user_from=request.user, user_to=person)
                        if qs.exists():
                            create_action(request.user, 'Unfollowed', person)
                            qs.first().delete()
                        else:
                            instance = Contact.objects.create(
                                user_from=request.user, user_to=person)
                            create_action(request.user, 'Followed', person)
                        return redirect('profiles:user-profile', slug=slug)
            else:
                return redirect('login')

    def get_context_data(self, *args, **kwargs):
        context = super(UserFollow, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        get_user = User.objects.filter(slug=slug)
        if get_user.exists():
            person = get_user.first()
            context['user'] = person
        profile = UserProfile.objects.get(user=person) or None
        if profile is not None:
            context['profile'] = profile
        return context


class CreateProfile(CreateView):
    template_name = "profiles/profile-create.html"
    form_class = ProfileForm

    def get_success_url(self):
        return reverse('profiles:user-profile', kwargs={'slug': self.user.slug})

    def dispatch(self, *args, **kwargs):
        request = self.request
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            if request.user.userprofile.active:
                return redirect('/')
            else:
                return super(CreateProfile, self).dispatch(*args, **kwargs)


def photo_upload_view(request, slug):
    if request.user.is_authenticated:
        get_user = User.objects.filter(slug=slug)
        print(get_user)
        if get_user.exists():
            user = get_user.first()
            if user == request.user:
                if len(request.FILES) > 0:
                    form = PhotoUploadForm(request.POST, request.FILES)
                    instance = form.instance
                    instance.user = request.user
                    instance.save()
                    return render(request, "profiles/user-profile.html", {"photo_form": form})
                else:
                    pass
            else:
                return HttpResponseForbidden("You are not the same user!!")
        else:
            return Http404("User does not exist")
    else:
        return redirect('login')
