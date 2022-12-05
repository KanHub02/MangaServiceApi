from users.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_superuser(username="adminadmin", password="adminadmin")
            print("Username - adminadmin\nPassword - adminadmin")
        except:
            print("Admin is create already")
