from django.conf.urls import url
from . import views
from . import sistema, modulo

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sistema/listar/$', sistema.listar, name='sistema_listar'),
	url(r'^modulo/listar/(?P<sistema_id>[0-9]+)/$', modulo.listar, name='modulo_listar'),
]