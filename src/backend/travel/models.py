from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
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


class Adventure(models.Model):
    unique_id = models.CharField(max_length=150, blank=True, null=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    continent = models.CharField(max_length=150, choices=continent_choices)
    country = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    start = models.DateField()
    end = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.unique_id}'


def create_id(sender, instance, *args, **kwargs):
    if instance:
        instance.unique_id = unique_id_generator(instance)


pre_save.connect(create_id, sender=Adventure)
