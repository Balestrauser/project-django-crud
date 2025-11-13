# core/urls.py
from django.urls import path
from . import views # Importa o arquivo views.py do app

urlpatterns = [
    path('funcionarios/cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    
    # Quando alguém acessar a URL "raiz" deste app, chame a view "lista_funcionarios"
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    
    # Quando alguém acessar a URL "alimentos/", chame a view "lista_alimentos"
    path('alimentos/', views.lista_alimentos, name='lista_alimentos'),
]