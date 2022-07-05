from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),

]