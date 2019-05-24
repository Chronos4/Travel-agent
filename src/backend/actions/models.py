from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
User = get_user_model()


class Action(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="actions", db_index=True)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    target_ct = models.ForeignKey(
        ContentType, blank=True, null=True, related_name="tager_obj", on_delete=models.CASCADE)
    target_id = models.CharField(
        null=True, blank=True, db_index=True, max_length=500)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user}-{self.verb}-{self.target}'
