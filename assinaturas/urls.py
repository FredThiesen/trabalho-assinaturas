from django.urls import path
from . import views

urlpatterns = [
    path('nova/', views.nova_assinatura, name='nova_assinatura'),
    path('', views.lista_assinaturas, name='lista_assinaturas'),
    path('<int:id>/clientes/', views.assinatura_por_clientes, name='assinatura_por_clientes'),
    path('<int:id>/deletar/', views.deletar_assinatura, name='deletar_assinatura'),
]
