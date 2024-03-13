from threading import Thread
import requests
from data.config import ADDRES
from django.core.management.utils import get_random_secret_key
import requests


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def save_user(message) -> int():
    post_data = {"username": str(message.from_user.id),
                 "first_name": str(message.from_user.first_name),
                 "last_name": str(message.from_user.last_name),
                 "password": str(get_random_secret_key())}
    url = f"{ADDRES}api/register/"
    response = requests.post(url, data=post_data)
    return response


def activate_user(id):
    post_data = {'username': str(id)}
    url = f'{ADDRES}api/register/activate-user/'
    response = requests.post(url, data=post_data)
    return response
