## Gestión SWP - DJango Python

Requisitos de software previamente instalado:

	+ Python 2.7
	+ Python PIP
	+ NodeJS - NPM - Gulp y Bower

Instalación de dependencias:

	$ sudo pip install -r requirements.txt && npm install && bower install 

Para la instalación de PyCrypto, descargar el archivo pycrypto-2.6.1.tar.gz, descomprimir, entrar al directoro e instalar:

	$ sudo python setup.py install

### Generar 'dist'
	
	$ gulp layout && gulp app && gulp error-css

Comandos de DJango

	$ django-admin startproject mysite
	$ python manage.py startapp polls
	$ sudo pip install -r requirements.txt
	$ python manage.py runserver 192.168.1.9:8080
	$ python manage.py makemigrations libros
	$ python manage.py migrate

### Fuentes externas de vistas HTML:

+ Home : https://bootsnipp.com/snippets/1BQNV
+ Login form : https://bootsnipp.com/snippets/featured/modal-login-with-jquery-effects
+ Contacto : https://bootsnipp.com/snippets/zD4p9
+ Footer : https://bootsnipp.com/snippets/GQmaP
+ Error404 : https://bootsnipp.com/snippets/OeKdM

### TODO

+ Validación del formulario de registro valida como correo no registrado en la base de datos si al final del correo se añade un espacio
+ El menú del sitio debe ser un backboneView con su propio model
+ Cuando se usa la validación de campos en forms del login el contenedor del todo el login no se expande con el contenido
+ Hacer que el login se comunique con el servidor mediante AJAX
+ Hacer el error 404 pero con backbone en las rutas marionette de la aplicación

---

 Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]