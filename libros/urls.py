from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^autor/listar/$', views.autor_listar, name='autor_listar'),
	url(r'^autor/guardar/$', views.autor_guardar, name='autor_guardar'),
	url(r'^categoria/listar/$', views.categoria_listar, name='categoria_listar'),
]