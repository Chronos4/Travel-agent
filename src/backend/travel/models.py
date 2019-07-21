import datetime
import pycountry
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from actions.utils import create_action
from backend.utilities import unique_id_generator
# Create your models here.

User = settings.AUTH_USER_MODEL


continent_choices = [
    ('asia', 'Asia'),
    ('africa', 'Africa'),
    ('north america', 'North America'),
    ('south america', 'South America'),
    ('antarctica', 'ANTARCTICA'),
    ('europe', 'Europe'),
    ('australia', 'Australia'),
]

countries = [(x.name, x.name) for x in pycountry.countries]


class AdventureManager(models.Manager):

    def join(self, request, unique_id):
        if request.user.is_authenticated:
            query = Adventure.objects.filter(unique_id=unique_id)
            if query.exists():
                obj = query.first()
                if request.user != obj.author:
                    filt = obj.users.all()
                    if request.user not in filt:
                        obj.users.add(request.user)
                        create_action(
                            request.user, 'Enrolled In Destination', obj)
                        return True
                    elif request.user in filt:
                        create_action(
                            request.user, 'Removed From Destination', obj)
                        obj.users.remove(request.user)
                        return False


class Adventure(models.Model):
    unique_id = models.CharField(max_length=150, blank=True, null=True)
    users = models.ManyToManyField(User, related_name="candidates")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author", blank=True, null=True)
    #continent = models.CharField(max_length=150, choices=continent_choices)
    country = models.CharField(max_length=150, choices=countries)
    image = models.ImageField(upload_to='destinations', blank=True, null=True)
    town = models.CharField(max_length=150)
    commentaries = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    start = models.DateField(default=datetime.datetime.now)
    end = models.DateField(default=datetime.datetime.now)
    active = models.BooleanField(default=True)

    objects = AdventureManager()

    def __str__(self):
        return f'{self.unique_id}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('travel:destination-detail', kwargs={'unique_id': self.unique_id})


def create_id(sender, instance, *args, **kwargs):
    if instance:
        if instance.unique_id is None:
            instance.unique_id = slugify(unique_id_generator(instance))


pre_save.connect(create_id, sender=Adventure)


class Destination_comment(models.Model):
    post = models.ForeignKey(
        Adventure, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user.first_name} on {self.post}'

    class Meta:
        ordering = ['-created']
