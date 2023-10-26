from django.urls import path
from galeria.views import galeria

urlpatterns = {
    path('galeria/', galeria),
}