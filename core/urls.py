from django.urls import path
from .views import index, galeria, sobremim, contato

urlpatterns = [
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path('sobre/', sobremim, name='about'),
    path('contato/', contato, name='contato' ),
  ]
