from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Passenger

@receiver(post_save, sender=User)
def create_passenger(sender, instance, created, **kwargs):
    """ auto-create passenger profile after sign-up."""
    if created:
        Passenger.objects.create(user=instance, email=instance.email) 

@receiver(post_save, sender=User)
def save_passenger(sender, instance, **kwargs):
    instance.passenger.save()
