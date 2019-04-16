from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='profile-images', blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    hobbies = models.CharField(max_length=1000, blank=True, null=True)
    places_been = models.TextField(blank=True, null=True)
    places_to = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} profile'

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'slug': self.user.slug})


def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        if instance:
            profile = UserProfile.objects.create(user=instance)
            profile.save()


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
