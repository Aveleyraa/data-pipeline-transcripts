# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos locales al contenedor
COPY . /app

# Instala las dependencias si existe requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando por defecto (puedes cambiarlo según tu aplicación)
CMD ["python", "app.py"]