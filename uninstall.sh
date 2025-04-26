#!/bin/bash

echo "🧹 Deteniendo y eliminando contenedores de QR VirusTotal Checker..."
docker-compose down --rmi all --volumes --remove-orphans
echo "✅ Todo ha sido limpiado correctamente."
