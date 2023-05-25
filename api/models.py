from django.db import models

# Create your models here.


class Cursos(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
    curso_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cursos'

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sexo = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    estoy_de_acuerdo = models.BooleanField()
    token = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre