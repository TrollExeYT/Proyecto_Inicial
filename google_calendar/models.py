
from django.db import models
from django.contrib.auth.models import User
from google.oauth2.credentials import Credentials
import json

class GoogleCredentials(models.Model):
    """Almacena las credenciales de OAuth 2.0 para un usuario."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='google_credentials')
    credentials_json = models.TextField()

    @property
    def credentials(self) -> Credentials:
        """Devuelve un objeto Credentials de Google."""
        return Credentials.from_authorized_user_info(json.loads(self.credentials_json))

    @credentials.setter
    def credentials(self, credentials_obj: Credentials):
        """Guarda el objeto Credentials en formato JSON."""
        self.credentials_json = credentials_obj.to_json()

    def __str__(self):
        return f"Credenciales de {self.user.username}"