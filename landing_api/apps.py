from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
import os
from django.conf import settings

class LandingApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing_api'

    def ready(self):
        if not firebase_admin._apps:
            cred_path = os.path.join(settings.BASE_DIR, "secrets", "landing-key.json")
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://restaurante-99f86-default-rtdb.firebaseio.com/'
            })
