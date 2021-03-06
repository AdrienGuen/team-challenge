from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^connexion$', views.connexion),
    url(r'^deconnexion$', views.deconnexion),
    url(r'^challenge/(?P<id>\d+)$', views.afficher_challenge),
    url(r'^rejoindre/(?P<id>\d+)$', views.rejoindre),
    url(r'^quitter_challenge/(?P<id>\d+)$', views.quitter_challenge),
    url(r'^mes_challenges$', views.mes_challenges),
]
