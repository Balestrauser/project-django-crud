# setup/urls.py
from django.contrib import admin
from django.urls import path, include # <-- 1. ADICIONE O 'include' AQUI

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. ADICIONE ESTA LINHA:
    # Isso diz ao Django: "Qualquer URL que o usuário acessar,
    # vá verificar se ela existe no arquivo 'core.urls'".
    path('', include('core.urls')), 
]
