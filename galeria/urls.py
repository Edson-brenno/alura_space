from django.urls import path
from galeria.views import imagem

urlpatterns = {
    path('imagem/', imagem),
}