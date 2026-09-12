from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Biblioteca",
        default_version='v1',
        description="API REST para gestionar autores, libros y prestamos",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
