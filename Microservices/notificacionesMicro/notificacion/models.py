from django.db import models

# Create your models here.
class Notificacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo