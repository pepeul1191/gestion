from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^categoria/listar/$', views.categoria_listar, name='categoria_listar'),
]