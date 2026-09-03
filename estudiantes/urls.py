from rest_framework import routers
from .api import EstudianteViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register('estudiantes', EstudianteViewSet, basename='estudiantes')
router.register('cursos', CursoViewSet, basename='cursos')
urlpatterns = router.urls