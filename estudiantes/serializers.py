from .models import Estudiante,Curso
from rest_framework import serializers
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'codigo')
        
class EstudianteSerializer(serializers.ModelSerializer):
    cursos = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), many=True, required=False
    )
    cursos_detalle = CursoSerializer(source='cursos', many=True, read_only=True) 
    def validate_nombre(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("El nombre no puede contener números.")
        return value
    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'apellido', 'email', 'carrera', 'fecha_inscripcion', 'cursos', 'cursos_detalle')
        read_only_fields = ('fecha_inscripción',)