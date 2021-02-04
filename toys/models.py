from django.db import models


class ActiveObjectsManager(models.Manager):
    def get_request(self):
        return super().get_queryset().filter(is_active=True)


class User(models.Model):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    objects = models.Manager()
    active_objects = ActiveObjectsManager()
