#Imagen de python
FROM python:3.9 

#Directotio de trabajo
WORKDIR /app

#Copiar el archivo de dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copiar el codigo al contenedor
COPY . .

#Exponer el puerto 5000
EXPOSE 5000

#Ejecutar el flask
CMD ["Python", "app.py"]