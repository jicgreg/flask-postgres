# flask-postgres
mini App para insercion de usuario,libro y control de prestamo. 

Para ejecutar el contenedor Postgres:
docker compose up -d flask_db

image.png


Para comprobar si el contenedor se está ejecutando:
docker compose logs
 
Para mostrar todos los contenedores (en ejecución y detenidos):
docker ps -a
 

Para probar la conexión db, utilice la siguiente configuración:
•	Anfitrión: localhost
•	Puerto: 5432
•	Usuario: postgres
•	Contraseña: postgres
•	Base de datos: Postgres

Para verificar la conexión a c base de datos. Usamos el software DBeaver
 

Para construir y ejecutar la aplicación Flask.
docker compose build
Docker compose up –build flask_app
 

Para comprobar si la imagen se ha creado correctamente:

	docker images


Ejecutar el servicio flask_app
	Sudo docker compose up flask_app


Ejecutar docker-compose y sus servicios

ejecutar nuestro stack de servicios en segundo plano, para eso basta con agregar la opción -d al final.
docker-compose up -d
 

Validar probar todo GET, POST, PUT,DELETE

