from rest_framework import serializers
from .models import Autor, Libro, Prestamo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'nacionalidad', 'fecha_nacimiento')


class LibroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    autor_detalle = AutorSerializer(source='autor', read_only=True)

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'isbn', 'anio_publicacion', 'autor', 'autor_detalle')


class PrestamoSerializer(serializers.ModelSerializer):
    libro = serializers.PrimaryKeyRelatedField(queryset=Libro.objects.all())
    libro_detalle = LibroSerializer(source='libro', read_only=True)
    usuario_detalle = serializers.StringRelatedField(source='usuario', read_only=True)

    class Meta:
        model = Prestamo
        fields = ('id', 'fecha_prestamo', 'fecha_devolucion', 'estado', 'libro', 'usuario', 'libro_detalle', 'usuario_detalle')
        read_only_fields = ('usuario',)
