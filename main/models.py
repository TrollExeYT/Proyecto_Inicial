from django.contrib.auth.models import User
from django.db import models

# Modelo de los eventos predeterminados
class Event(models.Model):
    name = models.CharField(max_length=30)
    photo_path = models.CharField(max_length=150)
    visible = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['name', 'photo_path']

    def __str__(self):
        return self.name

def calendar_photo_path(instance, filename):
    return f"/user_{instance.user.id}/{filename}"

# Calendarios
class Calendar(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Hay que buscar como usar el DEFAULT en la foto - B
    photo = models.ImageField(upload_to=calendar_photo_path, default='', blank=True, null=True)

    REQUIRED_FIELDS = ['user', 'name']

    def __str__(self):
        return f"{self.name} de {self.user.username}"

# Conectores y divisores de eventos
# Crear una view especifica para
class EventConnector(models.Model):
    DAYS = (
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miercoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sab y Dom'),
    )

    GROUPS = (
        (0, 'Dia'),
        (1, 'Tarde'),
        (2, 'Noche'),
    )

    DIVISIONS = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
    )

    day = models.SmallIntegerField(choices=DAYS)
    group = models.SmallIntegerField(choices=GROUPS)
    division = models.SmallIntegerField(choices=DIVISIONS)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['day', 'group', 'division', 'calendar', 'event']

    def position(self):
        return [self.day, self.group, self.division]

    def __str__(self):
        return self.event.name