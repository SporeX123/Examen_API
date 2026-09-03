from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    cursos = models.ManyToManyField(Curso, blank=True, related_name='estudiantes')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"