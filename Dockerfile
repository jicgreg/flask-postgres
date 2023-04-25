#Extrae la imagen base oficial
FROM python:3.6-slim-buster

#Directorio de trabajo
WORKDIR /app

#Instala dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt

#copiar proyecto
COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]