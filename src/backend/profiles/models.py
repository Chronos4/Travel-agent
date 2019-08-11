from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save, pre_save

# Create your models here.


class Contact(models.Model):
    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from.email} follows {self.user_to.email}'


# def check_for_now_already_following(sender, instance, *args, **kwargs):
#     #TODO change the function later
#     if instance:
#         qs = Contact.objects.filter(
#             user_from=instance.user_from, user_to=instance.user_to) or None
#         if qs.exists():
#             qs.first().delete()
#             return ValueError("Error")


# pre_save.connect(check_for_now_already_following, sender=Contact)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='profile-images', default='default-profile.png', blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    hobbies = models.CharField(max_length=1000, blank=True, null=True)
    places_been = models.TextField(blank=True, null=True)
    places_to = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.email} profile'

    def get_absolute_url(self):
        return reverse('profiles:user-profile', kwargs={'slug': self.user.slug})


def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        if instance:
            profile = UserProfile.objects.create(user=instance)
            profile.save()


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
