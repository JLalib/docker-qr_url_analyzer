# QR URL Analyzer con VirusTotal

Esta aplicación web permite al usuario **escanear un código QR** o **introducir manualmente una URL**, y luego **analiza la seguridad del enlace** utilizando la API de [VirusTotal](https://www.virustotal.com/).

## 🧰 Tecnologías utilizadas

- **Frontend**: HTML, TailwindCSS, JavaScript, HTML5 QR Scanner
- **Backend**: Python (Flask), requests
- **API**: VirusTotal v3
- **Contenedores**: Docker + Docker Compose
- **Servidor web**: NGINX (como proxy inverso)

---

## 🚀 ¿Qué puede hacer esta app?

- Escanear un código QR desde la cámara del móvil.
- Ingresar una URL manualmente.
- Consultar VirusTotal para:
  - Verificar si la URL es segura o maliciosa.
  - Mostrar detalles del análisis: harmless, suspicious, malicious, undetected.
  - Mostrar enlace directo al informe de VirusTotal.

---

## 📦 Requisitos

- Docker
- Docker Compose

---

## ⚙️ Instalación y ejecución

1. **Clona o descomprime este proyecto en tu servidor local**

```bash
unzip qr_virustotal_checker_detailed.zip
cd qr_virustotal_checker
```

2. **Ejecuta Docker Compose**

```bash
docker-compose up --build
```

3. **Accede a la app desde tu navegador**

```
http://localhost:8080
```

---

## 🔐 API Key de VirusTotal

Tu clave está definida directamente en el `docker-compose.yml` como variable de entorno:

```yaml
environment:
  - VT_API_KEY=tu_api_key_aqui
```

Para mayor seguridad en producción, puedes usar un archivo `.env` y referenciarlo con `env_file:`.

---

## 📁 Estructura del proyecto

```
qr_virustotal_checker/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── nginx.conf
└── docker-compose.yml
```

---

## 📌 Notas

- Si el escaneo QR falla, asegúrate de permitir el acceso a la cámara.
- El backend usa NGINX como proxy inverso, por lo tanto puedes comunicarte usando `fetch('/analyze')` sin problemas de CORS.
- El backend intentará recuperar un informe existente o enviar la URL para análisis si no hay datos previos.

---

## ✨ Licencia

Este proyecto es de uso libre para fines educativos o internos.
