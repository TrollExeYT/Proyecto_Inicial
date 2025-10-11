from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Modelo de los usuarios
class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'

    REQUIRED_FIELDS = ['username', 'password']

# Modelo de los eventos predeterminados
class Event(models.Model):
    name = models.CharField(max_length=30)
    photo_path = models.CharField(max_length=150)

    REQUIRED_FIELDS = ['name', 'photo_path']

# Calendarios
class Calendar(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Buscar manera de subir archivos para los calendarios o en caso contrario crear predeterminados
    # photo = models.ImageField()

    REQUIRED_FIELDS = ['user', 'name']

# Conectores y divisores de eventos
# Crear una view especifica para
class EventConnector(models.Model):
    DIVISIONS = (
        (0, 'Dia'),
        (1, 'Tarde'),
        (2, 'Noche'),
    )

    division = models.IntegerField(choices=DIVISIONS)
    subdivision = models.IntegerField() # del 0 al 2 sin repetir por calendario y division
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['calendar', 'event', 'division', 'subdivision']