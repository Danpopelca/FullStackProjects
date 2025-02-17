"""
URL configuration for SectionMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core.views import assign_sections_view, save_server  # Asigură-te că save_server este importat

urlpatterns = [
    path("", assign_sections_view, name="home"),  # ✅ Aceasta va fi pagina principală
    path("assign/", assign_sections_view, name="assign_sections"),
    path("save_server/", save_server, name="save_server"),
]
