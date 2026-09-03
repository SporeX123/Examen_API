from .models import Estudiante, Curso
from .serializers import EstudianteSerializer, CursoSerializer
from rest_framework import viewsets, permissions

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstudianteSerializer