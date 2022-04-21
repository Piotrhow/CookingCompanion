from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Pantry


@receiver(post_save, sender=User)
def create_pantry(sender, instance, created, **kwargs):
    if created:
        Pantry.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_pantry(sender, instance, **kwargs):
    instance.pantry.save()
