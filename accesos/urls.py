from django.conf.urls import url
from . import views
from . import sistema, modulo, subtitulo, item

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^sistema/listar/$', sistema.listar, name='sistema_listar'),
	url(r'^modulo/listar/(?P<sistema_id>[0-9]+)/$', modulo.listar, name='modulo_listar'),
	url(r'^subtitulo/listar/(?P<modulo_id>[0-9]+)/$', subtitulo.listar, name='subtitulo_listar'),
	url(r'^item/listar/(?P<subtitulo_id>[0-9]+)/$', item.listar, name='item_listar'),
]