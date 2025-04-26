#!/bin/bash

echo "🔄 Actualizando QR VirusTotal Checker..."

# Bajar contenedores sin borrar datos
docker-compose down

# Reconstruir y levantar
docker-compose up --build -d

echo "✅ Actualización completada."
