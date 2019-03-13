from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, age, active=True, staff=False, admin=False):
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

    def create_staffuser(self, email, password, first_name, last_name, age, active=True, staff=False, admin=False):
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

    def create_superuser(self, email, password, first_name, last_name, age, active=True, staff=False, admin=False):
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


class User(AbstractBaseUser):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    slug = models.SlugField(max_length=200)
    profile_image = models.ImageField(
        upload_to='profile-images', blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    hobbies = models.CharField(max_length=1000, blank=True, null=True)
    places_been = models.TextField(blank=True, null=True)
    places_to = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}--{self.last_name}--{self.first_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
