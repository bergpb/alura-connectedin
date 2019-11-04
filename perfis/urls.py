from django.urls import path
from perfis import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
    path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('perfis/<int:convite_id>/aceitar', views.aceitar, name='aceitar')
]
