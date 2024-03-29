"""turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from turismo import settings
from vitrines.views import VitrinesViewSet


# Documentação da API com swagger

schema_view = get_schema_view(
   openapi.Info(
      title="VITRINES API",
      default_version="v1",
      description="API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="suporte@google.org"),
      license=openapi.License(name="BSD License")
   ),
   public=False,
   permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vitrines/", VitrinesViewSet.as_view(), name="vitrines"),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="docs")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
