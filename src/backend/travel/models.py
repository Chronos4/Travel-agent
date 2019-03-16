from django.db import models
from django.conf import settings
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
    unique_id = models.CharField(max_length=150)
    user = models.ManyToManyField(User)
    continent = models.CharField(max_length=150, choices=continent_choices)
    country = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    when = models.DateField()

    def __str__(self):
        return f'{self.unique_id}'
