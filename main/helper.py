#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from .services import Services

class Helper:
	def __init__(self):
		self.services = Services()

		self.diccionario = {
			'BASE_URL': 'http://localhost:8000/',
			'STATICS_URL' : 'http://localhost:8000/static/',
			'ambiente': 'desarrollo',
			'nombre_app' : 'Aplicación Python Tornado',
			'cipher_key' : 's53hHaKFQoqXTDU9' 
		}

	def listar_modulos(self):
		url = self.services.get('accesos') + "modulo/listar_menu?sistema=SISTEMA_ACCESOS"
		response = requests.get(url)
		return response.text

	def listar_menu(self, modulo):
		url = self.services.get('accesos') + "item/listar/menu/" + modulo
		response = requests.get(url)
		return response.text

	def set(self, key, value):
		self.diccionario[key] = value

	def get(self, key):
		return self.diccionario[key]

	def array_to_json(self, string):
		rpta = []
		temps = json.loads(string)

		for temp in temps:
			rpta.append(json.loads(temp))

		return rpta
