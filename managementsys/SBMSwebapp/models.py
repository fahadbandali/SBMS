from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    who = models.CharField(default = "",max_length = 200)
    service = models.CharField(default = "",max_length = 200)
    when = models.DateTimeField(null=True, blank = True)
    cost = models.DecimalField(null = True, blank = True, max_digits=4, decimal_places=2)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()



