#!/bin/bash

echo "🚀 Iniciando instalación de QR VirusTotal Checker..."
docker-compose down
docker-compose up --build -d
echo "✅ Aplicación desplegada exitosamente."
echo "🌐 Accede a http://localhost:8080 en tu navegador."
