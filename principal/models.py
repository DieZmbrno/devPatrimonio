from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models

class PuntoInteres(models.Model):
    name = models.CharField(max_length=255)
    additionalInfo = models.TextField()
    imageURL = models.URLField()
    address = models.CharField(max_length=255)
    detailsPageURL = models.URLField()
    liveURL = models.URLField()
    geometria = models.PointField()

class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='default_password_value')
    username = models.CharField(max_length=150, unique=True, default='default_username_value')  # Cambia 'default_username_value' por un valor único

    # Agrega related_name para evitar la colisión de nombres
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='usuario_groups',
        related_query_name='usuario_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='usuario_user_permissions',
        related_query_name='usuario_user_permission',
    )

    def str(self):
        return self.email

class Calificacion(models.Model):
    idCalificacion = models.IntegerField(primary_key=True)
    puntuacion = models.IntegerField()
    fk_destino = models.ForeignKey('DestinoCultural', on_delete=models.CASCADE)

class HistorialVisitas(models.Model):
    idHistorial = models.AutoField(primary_key=True)
    destinoVisitados = models.CharField(max_length=255, default='default_destino_value')
    fk_destino = models.ForeignKey('DestinoCultural', on_delete=models.CASCADE, default=1)  # Cambia 1 por el ID del destino por defecto
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fk_usuario} - {self.destinoVisitados}'

class DestinoCultural(models.Model):
    idDestino = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imagenes = models.CharField(max_length=255)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentario(models.Model):
    idComentario = models.IntegerField(primary_key=True)
    texto = models.CharField(max_length=255)
    fk_destino = models.ForeignKey(DestinoCultural, on_delete=models.CASCADE)

class PreguntaInteractiva(models.Model):
    idPregunta = models.IntegerField(primary_key=True)
    texto = models.CharField(max_length=255)
    opciones = models.CharField(max_length=255)
    fk_destino = models.ForeignKey(DestinoCultural, on_delete=models.CASCADE)

class RecursoAdicional(models.Model):
    idRecurso = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    enlace = models.CharField(max_length=255)
    fk_destino = models.ForeignKey(DestinoCultural, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    idEvaluacion = models.IntegerField(primary_key=True)
    puntuacion = models.IntegerField()
    fecha = models.DateField()
    fk_destino = models.ForeignKey(DestinoCultural, on_delete=models.CASCADE)