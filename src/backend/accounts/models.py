from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import pre_save, m2m_changed
from backend.utilities import unique_slug_generator
from profiles.models import Contact
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, age=None, active=True, staff=False, admin=False):
        if email is None or password is None or first_name is None or last_name is None or age is None:
            raise ValueError('error none values my friend')
        user_object = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        user_object.set_password(password)
        user_object.staff = staff
        user_object.admin = admin
        user_object.active = active
        user_object.save(using=self._db)
        return user_object

    def create_staffuser(self, email, password=None, first_name=None, last_name=None, age=None):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            active=True,
            staff=True,
            admin=False
        )
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, age=None):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            active=True,
            staff=True,
            admin=True
        )
        return user


gender_choices = [
    ('male', 'Male'),
    ('female', 'Female')
]


class User(AbstractBaseUser):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.DateField()
    slug = models.SlugField(max_length=200, blank=True, null=True)
    following = models.ManyToManyField(
        'self', through=Contact, related_name="followers", symmetrical=False)
    gender = models.CharField(
        max_length=150, choices=gender_choices, blank=True, null=True)
    user_from_country = models.CharField(max_length=300, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}--{self.last_name}--{self.first_name}'

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def followers_count(self):
        return self.following.all().count()


def slug_create(sender, instance, *args, **kwargs):
    if instance:
        if instance.slug is None:
            instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_create, sender=User)


def m2m_changed_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_remove' or action == 'post_add' or action == 'post_clear':
        following = instance.following.all()
        followers = instance.followers.all()
        instance.following = following
        instance.followers = followers
        instance.save()


m2m_changed.connect(m2m_changed_receiver, sender=User)
