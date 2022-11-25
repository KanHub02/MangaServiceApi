from django.core.management.base import BaseCommand
from users.models import User

import random
import requests


# url = "https://api.реманга.орг/api/activity/comments/?title_id=2060&page=1&ordering=-id"
# domen2 = "https://api.реманга.орг/"
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
# }


# class Command(BaseCommand):
#     help = "Parsing data from manga sites, create users and comments"

#     def handle(self, *args, **kwargs):
#         response = requests.get(url=url, headers=HEADERS)
#         data = response.json()
#         for i in data["content"]:
#             User.objects.create_user(
#                 username=i["user"]["username"],
#                 password="useruser123",
#                 nickname=i["user"]["username"],
#                 image=domen2 + i["user"]["avatar"]["high"],
#             )


url = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org"

class Command(BaseCommand):
    help = "Parsing data from manga sites, create users and comments"

    def handle(self, *args, **kwargs):
        for page in range(20, 50):
            url = f"https://api.remanga.org/api/activity/comments/?title_id=8813&page={str(page)}&ordering=&count=20"
            

            response = requests.get(url=url, headers=HEADERS)
            data = response.json()
            for i in data["content"]:
                User.objects.create(
                    username=i["user"]["username"],
                    image=domen + i["user"]["avatar"]["high"],
                    nickname="#" + i["user"]["username"],
                    password="useruser123"
                )