from django.conf.urls import include, url
from sapl.audiencia.views import (index, AudienciaCrud, AnexoAudienciaPublicaCrud, busca_requerimento_por_parlamentar)

from .apps import AppConfig

app_name = AppConfig.name

urlpatterns = [
    url(r'^audiencia/', include(AudienciaCrud.get_urls() + AnexoAudienciaPublicaCrud.get_urls())),
    url('audiencia/busca_requerimento_por_parlamentar/', busca_requerimento_por_parlamentar),
]
