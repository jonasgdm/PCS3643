"""MyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('FIRST', views.bookview),
    # path('login', views.loginview),
    path('crud', views.crudview, name='crudview'),
    path('crud/create', views.crudcreateview, name='crudcreateview'),
    path('crud/delete/', views.crud_delete_list_view, name='crud_delete_list_view'),
    path('crud/delete/<str:idVoo>/', views.cruddeleteview, name='cruddeleteview'),
    path('crud/read', views.crudreadview, name='crudreadview'),
    path('crud/read/<str:idVoo>/', views.crud_read_specific_view, name='crud_read_specific_view'),
    path('crud/update/', views.crud_update_list_view, name='crud_update_list_view'),
    path('crud/update/<str:idVoo>/', views.crudupdateview, name='crudupdateview'),
    path('relatorio', views.relatorioview),
    path('painel-monitoracao/', views.painelview, name='painelview'),
    path('monitoracao-status', views.monitoracaoview),
    path('inicio-operador', views.operadorview),
    path('inicio-gerente', views.gerenteview),
    path('inicio-monitoracao/', views.funcionarioview, name='inicio_monit_view'),
]
