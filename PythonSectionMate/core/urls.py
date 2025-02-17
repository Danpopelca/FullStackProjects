from django.urls import path
from .views import assign_sections_view, save_server  # Asigură-te că save_server este importat

urlpatterns = [
    path("", assign_sections_view, name="home"),  # ✅ Aceasta va fi pagina principală
    path("assign/", assign_sections_view, name="assign_sections"),
    path("save_server/", save_server, name="save_server"),
]