from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Client  # Remplacez 'your_app' par le nom de votre application
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Transfère les utilisateurs non-staff vers la table Client'

    def handle(self, *args, **kwargs):
        non_staff_users = User.objects.filter(is_staff=False)
        for user in non_staff_users:
            # Vérifiez si le client existe déjà pour éviter les doublons
            if not Client.objects.filter(username=user.username).exists():
                client = Client(
                    username=user.username,
                    nom=user.first_name,
                    prenom=user.last_name,
                    email=user.email,
                    password=make_password(user.password)  # Hache le mot de passe
                )
                client.save()
                self.stdout.write(self.style.SUCCESS(f"Utilisateur {user.username} transféré vers Client."))
            else:
                self.stdout.write(self.style.WARNING(f"Utilisateur {user.username} déjà présent dans Client."))