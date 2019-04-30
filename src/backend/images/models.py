from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user/images', blank=True, null=True)
