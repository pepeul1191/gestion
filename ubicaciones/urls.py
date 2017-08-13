from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^distrito/buscar$', views.vw_distrito_provincia_departamento_buscar, name='vw_distrito_provincia_departamento_buscar'),
	url(r'^departamento/listar$', views.departamento_listar, name='departamento_listar'),
	url(r'^provincia/listar/(?P<departamento_id>[0-9]+)$', views.provincia_listar, name='provincia_listar'),
	url(r'^distrito/listar/(?P<provincia_id>[0-9]+)$', views.distrito_listar, name='distrito_listar'),
]