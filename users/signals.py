from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(**kwargs):
    print(kwargs)
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()