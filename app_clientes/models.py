from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

    def _str_ (self):
        return f"{self.nombre} {self.email}"