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
