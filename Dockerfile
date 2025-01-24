FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias con limpieza de caché
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . .

# Iniciar la aplicación Flask
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]
