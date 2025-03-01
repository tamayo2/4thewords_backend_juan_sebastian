# 4TheWords Backend - Juan Tamayo

Bienvenido al backend del proyecto **4TheWords**, un CRUD para un libro virtual de leyendas costarricenses. Este backend ha sido desarrollado utilizando **FastAPI** y **MySQL**, y está configurado para ejecutarse en un entorno virtual de Python.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework para construir APIs de alto rendimiento.
- **MySQL**: Base de datos relacional para almacenar la informacion.
- **Python**: Lenguaje principal del backend.
- **Uvicorn**: Servidor ASGI ligero y rapido para correr FastAPI.

---

## 📌 Requisitos Previos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas en tu sistema:

🔹 [Python 3.8 o superior](https://www.python.org/downloads/)  
🔹 [MySQL](https://www.mysql.com/)  
🔹 [Git](https://git-scm.com/)  
🔹 [pip](https://pip.pypa.io/en/stable/)  
🔹 (Opcional) [PyCharm](https://www.jetbrains.com/pycharm/) o tu editor preferido  

---

## 📥 Instalacion y Configuracion

Sigue estos pasos para configurar y ejecutar el backend en tu maquina local:

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/tamayo2/4thewords_backend_juan_sebastian.git
cd 4thewords_backend_juan_sebastian
```

### 2️⃣ Crear un Entorno Virtual

```bash
python -m venv venv
```

### 3️⃣ Activar el Entorno Virtual

**Windows:**  
```bash
venv\Scripts\activate
```

**MacOS/Linux:**  
```bash
source venv/bin/activate
```

### 4️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
pip install pydantic-settings
```

### 5️⃣ Crear la Base de Datos

Ejecuta el script SQL que se encuentra en la carpeta del backend para configurar la base de datos en MySQL.

### 6️⃣ Configurar la Conexion a la Base de Datos

Crea un archivo `.env` en la raiz del proyecto y agrega lo siguiente:

```plaintext
DATABASE_URL=mysql+mysqlconnector://usuario:contraseña@localhost/4thewords_prueba_juan_sebastian
```

_Reemplaza `usuario` y `contraseña` con tus credenciales de MySQL._

### 7️⃣ Ejecutar el Servidor de Desarrollo

Para iniciar el servidor en el puerto **8080**, usa el siguiente comando:

```bash
uvicorn api.main:api --host 127.0.0.1 --port 8080 --reload
```

---

## 🛠 Funcionalidades Principales

✅ CRUD de leyendas costarricenses  
✅ Autenticacion y autorizacion (futuras mejoras)  
✅ Conexion segura a MySQL con variables de entorno  
✅ Arquitectura modular para escalabilidad  

---

🚀 _Desarrollado con FastAPI y mucho codigo 💻_
