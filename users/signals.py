from django.contrib.auth.models import User
from .models import ProfileModel
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver (post_save,sender=User)
def create_profile(sender, instance,created,*args,**kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from .models import Client
from django.contrib.auth.hashers import make_password

def transfer_non_staff_users(sender, **kwargs):
    non_staff_users = User.objects.filter(is_staff=False)
    for user in non_staff_users:
        if not Client.objects.filter(username=user.username).exists():
            client = Client(
                username=user.username,
                nom=user.first_name,
                prenom=user.last_name,
                email=user.email,
                password=make_password(user.password)
            )
            client.save()

class usersAppConfig(AppConfig):
    name = 'users'

    def ready(self):
        post_migrate.connect(transfer_non_staff_users, sender=self)