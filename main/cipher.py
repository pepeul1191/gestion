#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import sys 
import random

def encode(texto):
	key = 'BIeEwOxk2vdFya6e'
	cipher = AES.new(key,AES.MODE_ECB)
	return base64.b64encode(cipher.encrypt(texto.rjust(32)))

def decode(texto):
	key = 'BIeEwOxk2vdFya6e'
	cipher = AES.new(key,AES.MODE_ECB)	
	return cipher.decrypt(base64.b64decode(texto)).strip()