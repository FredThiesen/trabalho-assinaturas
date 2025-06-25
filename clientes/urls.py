from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.cadastro_cliente, name='cadastro_cliente'),
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:id>/assinaturas/', views.cliente_assinaturas, name='cliente_assinaturas'),
]
