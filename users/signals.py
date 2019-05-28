from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is save send this signal, the receiver(decorator) will get this signal and call this function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


# need to create a method in apps for users:
#def ready(self):
#    import users.signals