from rest_framework import routers
from .api import AutorViewSet, LibroViewSet, PrestamoViewSet

router = routers.DefaultRouter()
router.register('autores', AutorViewSet, basename='autores')
router.register('libros', LibroViewSet, basename='libros')
router.register('prestamos', PrestamoViewSet, basename='prestamos')

urlpatterns = router.urls
