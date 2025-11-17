"""
URL configuration for empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rh import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # Produtos
    path('produtos/', views.lista_produtos, name='produtos'),

    # Rotas do app rh (outras URLs: clientes, funcionários, contato)
    path('', include('rh.urls')),

    # Blog
    path('blog/', include('blog.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

]

# Servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
