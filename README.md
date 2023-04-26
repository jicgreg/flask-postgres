# Mini app para control de prestamo de libros.

## **Introducción**

Crearemos una mini app que realiza operaciones CRUD en Python, usando el siguiente software:

***Flask*** 
Es un micro Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web bajo el patrón MVC.
MVC  permite diferenciar y separar lo que es el modelo de datos , es decir los datos que van a tener la App que normalmente están guardados en la base de datos, la vista,  la página HTML y el controlador donde se gestiona las peticiones de la app web.

***SQLAlchemy***
SQLAlchemy es el kit de herramientas SQL de Python y el mapeador relacional de objetos que ofrece a los desarrolladores de aplicaciones toda la potencia y flexibilidad de SQL.

***Postgres*** 
Es un potente sistema de base de datos relacional de objetos de código abierto
Docker para  separar las aplicaciones de la infraestructura y que pueda ejecutar rápidamente.
Docker file: Es un documento de texto que contiene todos los comandos
Docker Compose: Compose es una herramienta para definir y ejecutar aplicaciones Docker multicontenedor. Con Compose, se usa un archivo YAML para configurar los servicios de la aplicación.

***Operaciones CRUD***
 •	Crear
 •	Leer 
 •	Actualizar
 •	Borrar

## Pre-requisitos
	*Docker desktop
	*Sofware para validar conexión de la base de datos: ej Tableu, Dbeaver, PGAdmin4.
	*Software para validar operaciones CRUD: ej Postman, Testfully,Thunder Client, Postcode,Firecamp.

## Diagrama y arquitectura de la aplicación:

![Diagráma entidad relación](https://github.com/jicgreg/flask-postgres/blob/a6c4710ebea9a50f0445e38e11fa2bd26f29ab94/DER_mini_app.JPG)

![Componentes-Arquitectura](https://github.com/jicgreg/flask-postgres/blob/0fc81e6b35a583d35c3610d542f82ae86c538706/arquitectuta_flask_postgres_docker1.jpg)


## Pasos para la construcción:

1.	Crear una aplicación en Flask usando SQLALchemy para interactuar con la base de datos.
2.	Automatiza el despliegue de aplicaciones dentro de contenedores: creando un archivo Dockerfile y un archivo docker-compose para ejecutar la aplicación y la base de datos.
3.	Ejecutar la base de datos Postgres en un contenedor con Docker Compose.
Verificar la conexión a la base de dartos con cualquier software que nos de esta funcionalidad.
4.	Ejecutar la aplicación Flask en un contenedor con Docker compose.
Verificar las operaciones CRUD con Postman.


## Comandos para la ejecución:

Para ejecutar el contenedor Postgres:

	docker compose up -d flask_db

![flask_db](https://github.com/jicgreg/flask-postgres/blob/0bdde73870bb860f7b1a530c78297f85d0580779/flask_db.jpg)



Para comprobar si el contenedor se está ejecutando:
	
	docker compose logs
 
 ![logs](https://github.com/jicgreg/flask-postgres/blob/897051f84a9117752ed674cfab04eadc93ddcaab/logs.jpg)
 
Para mostrar todos los contenedores (en ejecución y detenidos):
	
	docker ps -a
 
![ps-a](https://github.com/jicgreg/flask-postgres/blob/cd1b1e367505101b59d835e7b8ebeb55dc43a0ab/ps-a.jpg)

Para probar la conexión db, utilizamos el software DBeaver con la siguiente configuración:

![conexion base de datos](https://github.com/jicgreg/flask-postgres/blob/997993e1ed46ad42d088d510c1ad1e170b57d991/conexion%20base%20de%20datos.jpg)


Para construir y ejecutar la aplicación Flask.

	docker compose up –build flask_app
 
 ![flas_app](https://github.com/jicgreg/flask-postgres/blob/d01e7e4cfec20c26c6806b3076cb6e3526b002d9/flask_app.jpg)

Para comprobar si la imagen se ha creado correctamente:

	docker images


Ejecutar el servicio flask_app
	
	Sudo docker compose up flask_app
![up flask_app](https://github.com/jicgreg/flask-postgres/blob/52dc251b95b041d2a71500bfd06593cd0f22ca45/up%20flask_app.jpg)


Ejecutar docker-compose y sus servicios
	
	docker-compose up -d
 
 
##Probar la aplicación

## Validar operaciones  GET, POST, PUT,DELETE

En cualquier navegador y visitemos localhost:4000/test o localhost:4000/


## Referencias
	*[SQLAlchemy - El kit de herramientas de base de datos para Python](https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion2/sqlalchemy.html)
	*[Flask Tutorials – Real Python](https://realpython.com/tutorials/flask/)
	*[PostgreSQL: La base de datos de código abierto más avanzada del mundo](https://www.postgresql.org/about/press/presskit14/es/) 
	*[Docker Compose overview | Docker Documentation](https://docs.docker.com/compose/)
	*[(Dockerfile reference | Docker Documentation](https://docs.docker.com/engine/reference/builder/) 
