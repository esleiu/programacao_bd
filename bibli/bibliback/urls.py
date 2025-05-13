from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .views import (
    LivroViewSet,
    UsuarioViewSet,
    MultaViewSet,
    EmprestimoViewSet,
    AutorViewSet,
    GeneroViewSet,
    EditoraViewSet,
    ReservaViewSet,
)
router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'multas', MultaViewSet)
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'autores',AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'reservas', ReservaViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API Laboratórios DIATINF",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]