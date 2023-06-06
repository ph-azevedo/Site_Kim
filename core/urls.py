from django.urls import path
from .views import index, galeria, sobremim, contato, navbar2

urlpatterns = [
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path('sobre/', sobremim, name='about'),
    path('contato/', contato, name='contato' ),
    path('navbar2/', navbar2, name='navbar2' ),
]